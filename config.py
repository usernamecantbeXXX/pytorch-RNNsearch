from yacs.config import CfgNode as CN 

_C = CN()

_C.SYSTEM = CN()
_C.SYSTEM.NUM_GPUS = 1

_C.TRAIN = CN()
_C.TRAIN.N_EPOCHS = 50
_C.TRAIN.BATCH_SIZE = 64

_C.VAL = CN()
_C.VAL.BATCH_SIZE = 32

_C.TEST = CN()
_C.TEST.BATCH_SIZE = 1

_C.OPTIMIZER = CN()
_C.OPTIMIZER.NAME = "ADADELTA"
_C.OPTIMIZER.LR = 1.0
_C.OPTIMIZER.RHO = 0.9
_C.OPTIMIZER.EPS = 0.000001
_C.OPTIMIZER.WEIGHT_DECAY = 0.9
_C.OPTIMIZER.CLIP = 1

_C.LR_SCHEDULER = CN()
_C.LR_SCHEDULER.NAME = "ReduceLROnPlateau"
_C.LR_SCHEDULER.MODE = "min"
_C.LR_SCHEDULER.FACTOR = 0.1
_C.LR_SCHEDULER.PATIENCE = 3
_C.LR_SCHEDULER.THRESHOLD = 0.00001

_C.MODEL = CN()
_C.MODEL.ENC_EMBED_DIM = 256
_C.MODEL.DEC_EMBED_DIM = 256
_C.MODEL.ENC_HIDDEN_DIM = 512
_C.MODEL.DEC_HIDDEN_DIM = 512
_C.MODEL.ENC_BIDIRECTIONAL = True
_C.MODEL.ENC_DROPOUT = 0.5
_C.MODEL.DEC_DROPOUT = 0.5

_C.DATASET = CN()
_C.DATASET.NAME = "IWSLT2017"
_C.DATASET.SRC_LANGUAGE = "de"
_C.DATASET.TGT_LANGUAGE = "en"
_C.DATASET.MIN_FREQ = 10
_C.DATASET.UNK_IDX = 0
_C.DATASET.PAD_IDX = 1
_C.DATASET.BOS_IDX = 2
_C.DATASET.EOS_IDX = 3
_C.DATASET.SPECIAL_SYMBOLS = ["unk", "pad", "bos", "eos"]


def get_cfg_defaults():
    """Get a yacs CfgNode object with default values"""
    return _C.clone()