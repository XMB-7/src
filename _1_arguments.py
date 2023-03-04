# 这段代码 如果出现在了单独脚本里面
# 那么就要使用%run 直接import不行 因为参数要在终端里面生成
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
    '--dates',
    type=list,
    default=(),
    # 要根据args.precip_periods来定值
    # 故而提前定义出来 等统一生成参数后 再赋予它具体数值
    # 这个变量不该作为参数出现 但不这样就加不进args 
    # 不知道有没有更好处理方案
    # 对于该模块的使用 仍然需要学习 ⁉️
    help='a list of tuples of all selected dates' 
)

parser.add_argument(
    '--files_rootdir',
    type=str,
    default='',
    # 要根据args.radar_id来定值
    help="root directory where radar sigmet files being located"
)

# #>> following arguments are set for plotting radar data files
# parser.add_argument(
#     '--field',
#     type=str,
#     default='reflectivity',
#     help='values of which field to be plotted'
# )
#
# parser.add_argument(
#     '--field_value_range',
#     type=tuple,
#     default=(0, 70),
#     help='field values only within (min, max) would be plotted'
# )
# parser.add_argument(
#     '--img_size',
#     type=tuple,
#     default=(128, 128),
#     help='plotted image size'
# )
# parser.add_argument(
#     '--grid_limits',
#     type=tuple,
#     default=((0e4, 2e4), (-3e5, 3e5), (-3e5, 3e5)),
#     help='''volume size centered around the radar to be plotted; in meters
#         for z, y, x coordinates'''
# )
# parser.add_argument(
#     '--grid_shape',
#     type=tuple,
#     default=(),
#     help='''the shape for each grid in the above volume, i.e. the number of 
#         points in the grid (z, y, x)'''
# ) 
# #<< ? 对这个参数理解还不到位
# #<< ? Cuomo's comment: define shape of frames (first dimension is Z)
# #<< ? 还得多看一看别人的代码
# parser.add_argument(
#     '--kernel_size',
#     type=tuple,
#     default=None,
#     help='''The size of the kernel used for convolving with an image 
#         to calculate the local average values indicating the precipitation intensity.
#         Just think of it as how big the clouds are considerd in the image.'''
# )
# parser.add_argument(
#     '--thresholds',
#     type=dict,
#     default={'frame': (30, 1), 'sequence': 1},
#     help='''The default threshold for frame is a tuple of ints, the first integer 
#         is in dBz for reflectivity data. (30, 1) indicates that a frame with 
#         at least 1 average field value in a local region exceeding 30dBz 
#         would be regarded as covering intense precipitation content.
#         The default threshold for sequence is an integer. 1 indicates that 
#         a sequence with at least 1 frame being regarded as covering intense 
#         precipitation content would be regarded as desired for training.'''
# )
# parser.add_argument(
#     '--img_root',
#     type=str,
#     default='',
#     help='the root derectory for all the plotted images'
# )
# parser.add_argument(
#     '--precip_sign',
#     type=str,
#     default='_P',
#     help='a sign indicating an image covers intense precipitation content'
# )

# #>> following arguments are set for constructing datasets
# parser.add_argument(
#     '--part_ratio',
#     type=float,
#     default=0.8,
#     help='partition ratio for spliting training set and validation set'
# )
# parser.add_argument(
#     '--n_inputs',
#     type=int,
#     default=20,
#     help='how many images used as inputs'
# )
# parser.add_argument(
#     '--n_outputs',
#     type=int,
#     default=20,
#     help='how many images to predict'
# )
# parser.add_argument(
#     '--n_seq',
#     type=int,
#     default=40,
#     help='how many images in a whole image sequence'
# )

# #>> following arguments are set for preparations for model training
# parser.add_argument(
#     '--batch_size',
#     type=int,
#     default=10,
#     help='how many image sequence samples in a batch used for model training'
# )
# parser.add_argument(
#     '--criterion',
#     type=tuple,
#     default=('MAE', 'MSE', 'Smooth_MAE'),
#     help='a tuple of different evaluation metrics for model training'
# )

# #>> following arguments are set for model training
# parser.add_argument(
#     '--model_archi',
#     type=str,
#     default='',
#     help='model architecture selected to implement nowcasting'
# )
# parser.add_argument(
#     '--loss_fn',
#     type=str,
#     default='',
#     help='loss function selected to evaluate the error.'
# )
# parser.add_argument(
#     '--cp_save_path',
#     type=str,
#     default='',
#     help='where checkpoint being saved to resume previous training'
# )

# parser.add_argument(
#     '--loss_records_save_dir',
#     type = str,
#     default = 'logs/loss_records',
#     help = 'dir where a loss record file is saved'
# )
# parser.add_argument(
#     '--pred_img_dir',
#     type = str,
#     default = 'logs/predictions',
#     help = 'dir where predicted images are saved'
# )

# parser.add_argument(
#     '--n_epoches',
#     type=int,
#     default=300,
#     help='how many times iterating through all examples'
# )

# parser.add_argument(
#     '--lr',
#     type = float,
#     default = 1e-3,
#     help = 'learning rate for training'
# )
# parser.add_argument(
#     '--wd',
#     type = float,
#     default = 5e-4,
#     help = 'weight decay for training'
# )
# # parser.add_argument(
# #     '--plot_grayscale',
# #     type=bool,
# #     default=True,
# #     help='True for plotting grayscale images and False for colorful images'
# # )
# #<< ? 这个东西就算要有 也应该是放到预测那里 
# #<< ? 提取的数据是2D数组 比如(128, 128) 
# #<< ? 所以前面绘图保存那一部分完全不需要绘制彩色图 没道理多存两个相同的2D矩阵

# 执行完该语句 各参数才真正被生成 >
# 然后才能对上述默认为空的参数赋值
args = parser.parse_args() 

# for downloading radar files >

args.precip_periods['month_1'] = [
('20200110_140000', '20200111_000000'),
# 似乎应该改成170000 好像是手误了 14-17都是晴天 但也无伤大雅
('20200111_000000', '20200111_150000'),
('20200116_090000', '20200117_000000'),
('20200117_000000', '20200118_000000'),
('20200122_000000', '20200123_000000'),
('20200128_000000', '20200129_000000')
]
args.precip_periods['month_2'] = [
('20200204_000000', '20200204_140000'),
('20200205_000000', '20200206_000000'), 
('20200210_000000', '20200211_000000'),
('20200212_000000', '20200212_180000')
]
args.precip_periods['month_3'] = [
('20200305_000000', '20200305_040000'),
('20200313_000000', '20200313_150000'),
('20200316_000000', '20200316_040000'),
('20200318_000000', '20200319_000000'),
('20200319_000000', '20200320_000000'),
('20200320_000000', '20200321_000000'), 
('20200321_200000', '20200322_000000'),
('20200322_000000', '20200322_120000'),
('20200328_040000', '20200328_220000'),
('20200330_000000', '20200331_000000')
]
args.precip_periods['month_4'] = [
('20200402_140000', '20200403_000000'),
('20200403_000000', '20200403_110000'),
('20200411_130000', '20200412_000000'),
('20200412_000000', '20200412_150000'),
('20200419_080000', '20200419_230000'),
('20200422_120000', '20200423_000000'),
('20200428_030000', '20200428_140000'),
]
args.precip_periods['month_5'] = [
('20200508_000000', '20200508_170000'),
('20200512_050000', '20200512_140000'),
('20200514_030000', '20200514_130000'),
('20200515_190000', '20200516_000000'),
('20200516_000000', '20200517_000000'),
('20200517_000000', '20200517_130000'),
('20200521_020000', '20200521_140000'),
('20200522_010000', '20200523_000000'),
('20200523_000000', '20200524_000000'),
('20200524_000000', '20200525_000000'),
('20200525_000000', '20200526_000000'),
('20200527_110000', '20200528_000000'),
('20200528_000000', '20200528_150000')
]
args.precip_periods['month_6'] = [
('20200605_000000', '20200605_130000'),
('20200619_150000', '20200620_000000'),
('20200620_000000', '20200620_200000'),
('20200621_040000', '20200621_220000'),
('20200622_050000', '20200622_170000'),
('20200623_040000', '20200624_000000'),
('20200624_000000', '20200625_000000'),
('20200630_000000', '20200630_070000')
]

dates = []
for month in args.precip_periods.keys():
    dates += [period[0][0: 8] for period in args.precip_periods[month]]
args.dates = dates

args.files_rootdir = f'../data/{args.radar_id}_Sigmet'
# 这是一个相对路径 其取决于该配置文件的位置

# #>> following arguments are set for plotting radar files
# args.grid_shape = (1, args.img_size[0], args.img_size[0])
# args.img_root = f'{args.radar_id}_Image_{args.img_size[0]}'

# #>> following arguments are set for constructing datasets for machine learning
# args.model_type = 'convlstm'


# args.model_save_path = f'logs/checkpoints/{args.model_type}.pth'


# args.n_seq = args.n_inputs + args.n_outputs