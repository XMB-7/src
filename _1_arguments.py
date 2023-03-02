import argparse
import os

path = '/net/nasstore/students/UNGRAD/UE/xbai/home/MyThesis/src'
os.chdir(path)

args = argparse.ArgumentParser()

#
# following arguments are set for downloading radar files
#

args.add_argument(
    '--radar_id',
    type=str,
    default='KFWS',
    help="which nexrad radar is the seleceted data being sampled from"
)

args.add_argument(
    '--precip_periods',
    type=dict,
    default={},
    # 稍后再行赋值 放这里太长了
    help="""a dict with months as keys and lists of tuples as values, 
        each representing a period of continuous precipitation 
        on a specific day in that month"""
)

# args.add_argument(
#     '--dates',
#     type=list,
#     default=(),
#     # 这个不该在这里定义 而是稍后往字典里面加 ❓
#     help='a list of tuples of all selected dates' 
# )

args.add_argument(
    '--files_rootdir',
    type=str,
    default='',
    help='root directory where radar sigmet files being located'
)

# #>> following arguments are set for plotting radar data files
# args.add_argument(
#     '--field',
#     type=str,
#     default='reflectivity',
#     help='values of which field to be plotted'
# )
#
# args.add_argument(
#     '--field_value_range',
#     type=tuple,
#     default=(0, 70),
#     help='field values only within (min, max) would be plotted'
# )
# args.add_argument(
#     '--img_size',
#     type=tuple,
#     default=(128, 128),
#     help='plotted image size'
# )
# args.add_argument(
#     '--grid_limits',
#     type=tuple,
#     default=((0e4, 2e4), (-3e5, 3e5), (-3e5, 3e5)),
#     help='''volume size centered around the radar to be plotted; in meters
#         for z, y, x coordinates'''
# )
# args.add_argument(
#     '--grid_shape',
#     type=tuple,
#     default=(),
#     help='''the shape for each grid in the above volume, i.e. the number of 
#         points in the grid (z, y, x)'''
# ) 
# #<< ? 对这个参数理解还不到位
# #<< ? Cuomo's comment: define shape of frames (first dimension is Z)
# #<< ? 还得多看一看别人的代码
# args.add_argument(
#     '--kernel_size',
#     type=tuple,
#     default=None,
#     help='''The size of the kernel used for convolving with an image 
#         to calculate the local average values indicating the precipitation intensity.
#         Just think of it as how big the clouds are considerd in the image.'''
# )
# args.add_argument(
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
# args.add_argument(
#     '--img_root',
#     type=str,
#     default='',
#     help='the root derectory for all the plotted images'
# )
# args.add_argument(
#     '--precip_sign',
#     type=str,
#     default='_P',
#     help='a sign indicating an image covers intense precipitation content'
# )

# #>> following arguments are set for constructing datasets
# args.add_argument(
#     '--part_ratio',
#     type=float,
#     default=0.8,
#     help='partition ratio for spliting training set and validation set'
# )
# args.add_argument(
#     '--n_inputs',
#     type=int,
#     default=20,
#     help='how many images used as inputs'
# )
# args.add_argument(
#     '--n_outputs',
#     type=int,
#     default=20,
#     help='how many images to predict'
# )
# args.add_argument(
#     '--n_seq',
#     type=int,
#     default=40,
#     help='how many images in a whole image sequence'
# )

# #>> following arguments are set for preparations for model training
# args.add_argument(
#     '--batch_size',
#     type=int,
#     default=10,
#     help='how many image sequence samples in a batch used for model training'
# )
# args.add_argument(
#     '--criterion',
#     type=tuple,
#     default=('MAE', 'MSE', 'Smooth_MAE'),
#     help='a tuple of different evaluation metrics for model training'
# )

# #>> following arguments are set for model training
# args.add_argument(
#     '--model_archi',
#     type=str,
#     default='',
#     help='model architecture selected to implement nowcasting'
# )
# args.add_argument(
#     '--loss_fn',
#     type=str,
#     default='',
#     help='loss function selected to evaluate the error.'
# )
# args.add_argument(
#     '--cp_save_path',
#     type=str,
#     default='',
#     help='where checkpoint being saved to resume previous training'
# )

# args.add_argument(
#     '--loss_records_save_dir',
#     type = str,
#     default = 'logs/loss_records',
#     help = 'dir where a loss record file is saved'
# )
# args.add_argument(
#     '--pred_img_dir',
#     type = str,
#     default = 'logs/predictions',
#     help = 'dir where predicted images are saved'
# )

# args.add_argument(
#     '--n_epoches',
#     type=int,
#     default=300,
#     help='how many times iterating through all examples'
# )

# args.add_argument(
#     '--lr',
#     type = float,
#     default = 1e-3,
#     help = 'learning rate for training'
# )
# args.add_argument(
#     '--wd',
#     type = float,
#     default = 5e-4,
#     help = 'weight decay for training'
# )
# # args.add_argument(
# #     '--plot_grayscale',
# #     type=bool,
# #     default=True,
# #     help='True for plotting grayscale images and False for colorful images'
# # )
# #<< ? 这个东西就算要有 也应该是放到预测那里 
# #<< ? 提取的数据是2D数组 比如(128, 128) 
# #<< ? 所以前面绘图保存那一部分完全不需要绘制彩色图 没道理多存两个相同的2D矩阵

# args = args.parse_args() 
# #<< 到终端上才能执行这一语句 从而真正生成参数
# #<< 然后才能接着设置那些需要用到其他参数的取值的参数的取值

#
# following arguments are set for downloading radar files
#
args.precip_periods['month_1'] = (
('20200110_140000', '20200111_000000'),
# 似乎应该改成170000 好像是失误了 前面都是晴天 但也无伤大雅
('20200111_000000', '20200111_150000'),
('20200116_090000', '20200117_000000'),
('20200117_000000', '20200118_000000'),
('20200122_000000', '20200123_000000'),
('20200128_000000', '20200129_000000')
)
args.precip_periods['month_2'] = (
('20200204_000000', '20200204_140000'),
('20200205_000000', '20200206_000000'), 
('20200210_000000', '20200211_000000'),
('20200212_000000', '20200212_180000')
)
args.precip_periods['month_3'] = (
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
)
args.precip_periods['month_4'] = (
('20200402_140000', '20200403_000000'),
('20200403_000000', '20200403_110000'),
('20200411_130000', '20200412_000000'),
('20200412_000000', '20200412_150000'),
('20200419_080000', '20200419_230000'),
('20200422_120000', '20200423_000000'),
('20200428_030000', '20200428_140000'),
)
args.precip_periods['month_5'] = (
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
)
args.precip_periods['month_6'] = (
('20200605_000000', '20200605_130000'),
('20200619_150000', '20200620_000000'),
('20200620_000000', '20200620_200000'),
('20200621_040000', '20200621_220000'),
('20200622_050000', '20200622_170000'),
('20200623_040000', '20200624_000000'),
('20200624_000000', '20200625_000000'),
('20200630_000000', '20200630_070000')
)
# temp_list = []
# for month in args.precip_periods.keys():
#     temp_list += [period[0][0: 10] for period in args.precip_periods[month]]
# args.dates = tuple(temp_list)
# #<< 借助args.precip_periods取值 设置args.dates取值
# #<< 注意元组是不能扩容的 所以要临时用一个列表来过渡一下
# args.file_root = f'{args.radar_id}_Sigmet'
# #<< ? 这里仍是一个相对路径 稍后建议还是改成绝对路径

# #>> following arguments are set for plotting radar files
# args.grid_shape = (1, args.img_size[0], args.img_size[0])
# args.img_root = f'{args.radar_id}_Image_{args.img_size[0]}'

# #>> following arguments are set for constructing datasets for machine learning
# args.model_type = 'convlstm'


# args.model_save_path = f'logs/checkpoints/{args.model_type}.pth'


# args.n_seq = args.n_inputs + args.n_outputs

# os.chdir(args.working_dir)