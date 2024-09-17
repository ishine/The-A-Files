from enum import Enum, auto


class MethodType(Enum):
    LSB_METHOD = auto()
    DCT_B1_METHOD = auto()
    NORM_SPACE_METHOD = auto()
    PHASE_CODING_METHOD = auto()
    DCT_DELTA_LSB_METHOD = auto()
    ECHO_METHOD = auto()
    DWT_LSB_METHOD = auto()
    DSSS_METHOD = auto()
    PATCHWORK_MULTILAYER_METHOD = auto()
    FSVC_METHOD = auto()


class MetricType(Enum):
    WSS_METRIC = auto()
    SNR_SEG_METRIC = auto()
    SNR_METRIC = auto()
    CEPSTRUM_DISTANCE_METRIC = auto()
    LLR_METRIC = auto()
    PESQ_METRIC = auto()
    FWSNR_SEG_METRIC = auto()
    MEL_CEPSTRAL_DISTANCE_METRIC = auto()
    BSD_METRIC = auto()
    SRMR_METRIC = auto()
    STOI_METRIC = auto()
    CSII_METRIC = auto()
    NCM_METRIC = auto()
    CBAK_METRIC = auto()
    CSIG_METRIC = auto()
    COVL_METRIC = auto()
    STGI_METRIC = auto()
    WSTMI_METRIC = auto()
    SISDR_METRIC = auto()
    BSS_EVAL_METRIC = auto()
    AI_MOSNET_METRIC = auto()
