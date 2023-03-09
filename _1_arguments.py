# 以下这段代码 如果单独出现在了脚本里面
# 就要使用%run 直接import不行 参数要在终端里面才能生成
# 但这就要求是ipython 该怎么办 
# 如果是直接执行命令行指令 !python args.py 它的结果又不继承
# 难道只能把它们存入主程序之中 ⁉️

import argparse

parser = argparse.ArgumentParser()

# for downloading radar files >

parser.add_argument(
    '--radar_id',
    type=str,
    default='KFWS',
    help="which nexrad radar is the seleceted data being sampled from"
)

parser.add_argument(
    '--precip_periods',
    type=dict,
    default={},
    # 稍后再行赋值 放这里太长了
    help="""a dict with months as keys and lists of tuples as values, 
        each representing a period of continuous precipitation 
        on a specific day in that month"""
)

parser.add_argument(
    '--data_dir',
    type=str,
    default='',
    # 要根据args.radar_id来定值
    # 故而提前定义出来 等统一生成参数后 再赋予它具体数值
    help="root directory where radar sigmet files being located"
)

# for plotting radar data files and saving >

parser.add_argument(
    '--field',
    type=str,
    default='reflectivity',
    help="values of which field to be plotted"
)

parser.add_argument(
    '--field_value_range',
    type=tuple,
    default=(0, 70),
    help="values out of this range would be filtered out"
)

parser.add_argument(
    '--img_size',
    type=tuple,
    default=(128, 128),
    help="image size for plotting"
)

parser.add_argument(
    '--grid_limits',
    type=tuple,
    default=((0e4, 2e4), (-3e5, 3e5), (-3e5, 3e5)),
    help="""volume size centered around the radar to be plotted; in meters
        for z, y, x coordinates"""
)

parser.add_argument(
    '--grid_shape',
    # 要根据args.img_size来定值
    # 实际只是让其等于args.img_size
    type=tuple,
    default=(),
    help="""the shape for each grid in the above volume, i.e. the number of 
        points in the grid (z, y, x)"""
) 
# Cuomo's comment: define shape of frames (first dimension is Z)
# 其实就是一格对应多大地盘 注意这跟把图画成多大是两码事
# 只不过这里就取等大了
# 由于是平面图 所以第一维度是一 详见下文

parser.add_argument(
    '--kernel_size',
    type=tuple,
    default=None,
    help="""The size of the kernel used for convolving with an image 
        to calculate the local average values indicating the precipitation intensity.
        Just think of it as how big the clouds are considerd in the image."""
)

parser.add_argument(
    '--thresholds',
    type=dict,
    default={'for_frame': (30, 1), 'for_sequence': 1},
    help="""The default threshold for frame is a tuple of ints, the first integer 
        is in dBz for reflectivity data. (30, 1) indicates that a frame with 
        at least 1 average field value in a local region exceeding 30dBz 
        would be regarded as covering intense precipitation content.
        The default threshold for sequence is an integer. 1 indicates that 
        a sequence with at least 1 frame being regarded as covering intense 
        precipitation content would be regarded as desired for training."""
)

parser.add_argument(
    '--img_dir',
    type=str,
    default='',
    help='the root derectory for all the plotted images'
)

parser.add_argument(
    '--precip_sign',
    type=str,
    default='_P',
    help='a sign indicating an image covers intense precipitation content'
)

# for dataset construction  >

parser.add_argument(
    '--part_ratio',
    type=float,
    default=0.8,
    help='partition ratio for spliting training set and validation set'
)

parser.add_argument(
    '--n_inputs',
    type=int,
    default=6,
    help='how many images used as inputs'
)

parser.add_argument(
    '--n_outputs',
    type=int,
    default=18,
    help='how many images to predict'
)

parser.add_argument(
    '--n_seq',
    # 要根据args.n_inputs和n_outputs来定值
    type=int,
    default=30,
    help='how many images form a sequence instance'
)

# for preparations on model training >

parser.add_argument(
    '--batch_size',
    type=int,
    default=32,
    help='how many image sequence samples in a batch used for model training'
)

parser.add_argument(
    '--criterion',
    type=tuple,
    default=('MAE', 'MSE', 'Smooth_MAE', 'SSIM'),
    help='a tuple of different evaluation metrics for model training'
)

# for model training >

parser.add_argument(
    '--n_epoches',
    type=int,
    default=200,
    help='how many times iterating through all examples'
)

parser.add_argument(
    '--lr',
    type = float,
    default = 1e-3,
    help = 'learning rate for training'
)

parser.add_argument(
    '--wd',
    type = float,
    default = 5e-4,
    help = 'weight decay for training'
)

parser.add_argument(
    '--model_archi',
    type=tuple,
    default=('ConvLSTM', 'ConvGRU', 'NeuralODE'),
    help='model architectures implemented for weather nowcasting'
)

parser.add_argument(
    '--model_selected',
    type=tuple,
    default='ConvLSTM',
    help='model architecture selected to implement weather nowcasting'
)
parser.add_argument(
    '--log_dir',
    # 要根据args.model_selected来定值
    type=str,
    default='',
    help='where generated log files will locate in'
)


parser.add_argument(
    '--ckpt_dir',
    # 要根据args.model_archi来定值
    type=str,
    default='',
    help='where checkpoints being saved to resume previous training'
)

parser.add_argument(
    '--loss_records_save_dir',
    type = str,
    default = '../logs/loss_records',
    help = 'dir where a loss record file is saved'
)

parser.add_argument(
    '--pred_img_dir',
    type = str,
    default = '../logs/predictions',
    help = 'dir where predicted images are saved'
)



# 执行完该语句 各参数才真正被生成 >
# 然后才能对上述默认为空的参数赋值 以及往字典里加值
args = parser.parse_args() 

# for downloading radar files >

# args.precip_periods['month_1'] = [
# ('20200110_140000', '20200111_000000'),
# # 似乎应该改成170000 好像是手误了 14-17都是晴天 但也无伤大雅
# ('20200111_000000', '20200111_150000'),
# ('20200116_090000', '20200117_000000'),
# ('20200117_000000', '20200118_000000'),
# ('20200122_000000', '20200123_000000'),
# ('20200128_000000', '20200129_000000')
# ]
# args.precip_periods['month_2'] = [
# ('20200204_000000', '20200204_140000'),
# ('20200205_000000', '20200206_000000'), 
# ('20200210_000000', '20200211_000000'),
# ('20200212_000000', '20200212_180000')
# ]
# args.precip_periods['month_3'] = [
# ('20200305_000000', '20200305_040000'),
# ('20200313_000000', '20200313_150000'),
# ('20200316_000000', '20200316_040000'),
# ('20200318_000000', '20200319_000000'),
# ('20200319_000000', '20200320_000000'),
# ('20200320_000000', '20200321_000000'), 
# ('20200321_200000', '20200322_000000'),
# ('20200322_000000', '20200322_120000'),
# ('20200328_040000', '20200328_220000'),
# ('20200330_000000', '20200331_000000')
# ]
# args.precip_periods['month_4'] = [
# ('20200402_140000', '20200403_000000'),
# ('20200403_000000', '20200403_110000'),
# ('20200411_130000', '20200412_000000'),
# ('20200412_000000', '20200412_150000'),
# ('20200419_080000', '20200419_230000'),
# ('20200422_120000', '20200423_000000'),
# ('20200428_030000', '20200428_140000'),
# ]
# args.precip_periods['month_5'] = [
# ('20200508_000000', '20200508_170000'),
# ('20200512_050000', '20200512_140000'),
# ('20200514_030000', '20200514_130000'),
# ('20200515_190000', '20200516_000000'),
# ('20200516_000000', '20200517_000000'),
# ('20200517_000000', '20200517_130000'),
# ('20200521_020000', '20200521_140000'),
# ('20200522_010000', '20200523_000000'),
# ('20200523_000000', '20200524_000000'),
# ('20200524_000000', '20200525_000000'),
# ('20200525_000000', '20200526_000000'),
# ('20200527_110000', '20200528_000000'),
# ('20200528_000000', '20200528_150000')
# ]
# args.precip_periods['month_6'] = [
# ('20200605_000000', '20200605_130000'),
# ('20200619_150000', '20200620_000000'),
# ('20200620_000000', '20200620_200000'),
# ('20200621_040000', '20200621_220000'),
# ('20200622_050000', '20200622_170000'),
# ('20200623_040000', '20200624_000000'),
# ('20200624_000000', '20200625_000000'),
# ('20200630_000000', '20200630_070000')
# ]

args.precip_periods["month_1"] = [
("2020-01-10:17:00:00", "2020-01-11:00:00:00"),
("2020-01-11:00:00:00", "2020-01-11:15:00:00"),
("2020-01-16:09:00:00", "2020-01-17:00:00:00"),
("2020-01-17:00:00:00", "2020-01-18:00:00:00"),
("2020-01-22:00:00:00", "2020-01-23:00:00:00"),
("2020-01-28:00:00:00", "2020-01-29:00:00:00")
]
args.precip_periods["month_2"] = [
("2020-02-04:00:00:00", "2020-02-04:14:00:00"),
("2020-02-05:00:00:00", "2020-02-06:00:00:00"), 
("2020-02-10:00:00:00", "2020-02-11:00:00:00"),
("2020-02-12:00:00:00", "2020-02-12:18:00:00")
]
args.precip_periods["month_3"] = [
("2020-03-05:00:00:00", "2020-03-05:04:00:00"),
("2020-03-13:00:00:00", "2020-03-13:15:00:00"),
("2020-03-16:00:00:00", "2020-03-16:04:00:00"),
("2020-03-18:00:00:00", "2020-03-19:00:00:00"),
("2020-03-19:00:00:00", "2020-03-20:00:00:00"),
("2020-03-20:00:00:00", "2020-03-21:00:00:00"), 
("2020-03-21:20:00:00", "2020-03-22:00:00:00"),
("2020-03-22:00:00:00", "2020-03-22:12:00:00"),
("2020-03-28:04:00:00", "2020-03-28:22:00:00"),
("2020-03-30:00:00:00", "2020-03-31:00:00:00")
]
args.precip_periods["month_4"] = [
("2020-04-02:14:00:00", "2020-04-03:00:00:00"),
("2020-04-03:00:00:00", "2020-04-03:11:00:00"),
("2020-04-11:13:00:00", "2020-04-12:00:00:00"),
("2020-04-12:00:00:00", "2020-04-12:15:00:00"),
("2020-04-19:08:00:00", "2020-04-19:23:00:00"),
("2020-04-22:12:00:00", "2020-04-23:00:00:00"),
("2020-04-28:03:00:00", "2020-04-28:14:00:00"),
]
args.precip_periods["month_5"] = [
("2020-05-08:00:00:00", "2020-05-08:17:00:00"),
("2020-05-12:05:00:00", "2020-05-12:14:00:00"),
("2020-05-14:03:00:00", "2020-05-14:13:00:00"),
("2020-05-15:19:00:00", "2020-05-16:00:00:00"),
("2020-05-16:00:00:00", "2020-05-17:00:00:00"),
("2020-05-17:00:00:00", "2020-05-17:13:00:00"),
("2020-05-21:02:00:00", "2020-05-21:14:00:00"),
("2020-05-22:01:00:00", "2020-05-23:00:00:00"),
("2020-05-23:00:00:00", "2020-05-24:00:00:00"),
("2020-05-24:00:00:00", "2020-05-25:00:00:00"),
("2020-05-25:00:00:00", "2020-05-26:00:00:00"),
("2020-05-27:11:00:00", "2020-05-28:00:00:00"),
("2020-05-28:00:00:00", "2020-05-28:15:00:00")
]
args.precip_periods["month_6"] = [
("2020-06-05:00:00:00", "2020-06-05:13:00:00"),
("2020-06-19:15:00:00", "2020-06-20:00:00:00"),
("2020-06-20:00:00:00", "2020-06-20:20:00:00"),
("2020-06-21:04:00:00", "2020-06-21:22:00:00"),
("2020-06-22:05:00:00", "2020-06-22:17:00:00"),
("2020-06-23:04:00:00", "2020-06-24:00:00:00"),
("2020-06-24:00:00:00", "2020-06-25:00:00:00"),
("2020-06-30:00:00:00", "2020-06-30:07:00:00")
]

dates = []
for month in args.precip_periods.keys():
    # dates += [period[0][0: 8] for period in args.precip_periods[month]]
    dates += [period[0][0: 10] for period in args.precip_periods[month]]
args.dates = dates

args.data_dir = f'../data/{args.radar_id}_Sigmet'
# 这是一个相对路径 其取决于该配置文件的位置

# for plotting radar files >
args.grid_shape = (1, args.img_size[0], args.img_size[0])
args.img_dir = f'../data/{args.radar_id}_Image_{args.img_size[0]}'

# for constructing datasets for machine learning >

args.n_seq = args.n_inputs + args.n_outputs

args.log_dir = f'../logs/{args.model_selected}'
args.ckpt_dir = f'{args.log_dir}/checkpoints'
