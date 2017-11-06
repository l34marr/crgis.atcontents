#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from crgis.atcontents import atcontentsMessageFactory as _


class data_src(object):
    """ Data Source
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='governmental', title=_(u'Governmental')),
            SimpleTerm(value='academic', title=_(u'Academic')),
            SimpleTerm(value='fieldwork', title=_(u'Fieldwork')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
data_srcFactory = data_src()

class coordinate(object):
    """ Coordinate Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='address', title=_(u'GeoCoder')),
            SimpleTerm(value='gps', title=_(u'GPS')),
            SimpleTerm(value='gisref', title=_(u'GIS Reference')),
            SimpleTerm(value='map', title=_(u'Map')),
            SimpleTerm(value='notyet', title=_(u'Not Yet')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
coordinateFactory = coordinate()

class deity_name(object):
    """ Deity Name
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='deity_001', title=_(u'WangYe')),
            SimpleTerm(value='deity_002', title=_(u'ChengHuang')),
            SimpleTerm(value='deity_003', title=_(u'TuDiGong')),
            SimpleTerm(value='deity_004', title=_(u'YingShen')),
            SimpleTerm(value='deity_005', title=_(u'MaZu')),
            SimpleTerm(value='deity_006', title=_(u'SanTaiZi')),
            SimpleTerm(value='deity_007', title=_(u'BaoShengDD')),
            SimpleTerm(value='deity_008', title=_(u'XuanTienDD')),
            SimpleTerm(value='deity_009', title=_(u'WuGuDD')),
            SimpleTerm(value='deity_010', title=_(u'GuangZeZW')),
            SimpleTerm(value='deity_011', title=_(u'GuanSengDJ')),
            SimpleTerm(value='deity_012', title=_(u'GuanShiYin')),
            SimpleTerm(value='deity_013', title=_(u'YuHuangDD')),
            SimpleTerm(value='deity_014', title=_(u'WangMuNN')),
            SimpleTerm(value='deity_015', title=_(u'SanGuanDD')),
            SimpleTerm(value='deity_016', title=_(u'SanNaiFR')),
            SimpleTerm(value='deity_017', title=_(u'LinSueiFR')),
            SimpleTerm(value='deity_018', title=_(u'ZhengChenGong')),
            SimpleTerm(value='deity_019', title=_(u'SanShanGW')),
            SimpleTerm(value='deity_020', title=_(u'QingSheiZS')),
            SimpleTerm(value='deity_021', title=_(u'ChanKueiZS')),
            SimpleTerm(value='deity_022', title=_(u'SanPingZS')),
            SimpleTerm(value='deity_023', title=_(u'JiouTianNN')),
            SimpleTerm(value='deity_024', title=_(u'JiGongZS')),
            SimpleTerm(value='deity_025', title=_(u'KaiZhangSW')),
            SimpleTerm(value='deity_026', title=_(u'ZhangXun')),
            SimpleTerm(value='deity_027', title=_(u'XuYuan')),
            SimpleTerm(value='deity_028', title=_(u'ZhengBaoHuei')),
            SimpleTerm(value='deity_029', title=_(u'XieAn')),
            SimpleTerm(value='deity_030', title=_(u'XieXuan')),
            SimpleTerm(value='deity_031', title=_(u'QiXingNN')),
            SimpleTerm(value='deity_032', title=_(u'QiZhuXS')),
            SimpleTerm(value='deity_033', title=_(u'SiMingZJ')),
            SimpleTerm(value='deity_034', title=_(u'JiouFuXS')),
            SimpleTerm(value='deity_035', title=_(u'JiouHuangDD')),
            SimpleTerm(value='deity_036', title=_(u'JiouLianFZ')),
            SimpleTerm(value='deity_037', title=_(u'JiouLongSG')),
            SimpleTerm(value='deity_038', title=_(u'ErLangSJ')),
            SimpleTerm(value='deity_039', title=_(u'BaGuaZS')),
            SimpleTerm(value='deity_040', title=_(u'ShiErNNN')),
            SimpleTerm(value='deity_041', title=_(u'SanYiXS')),
            SimpleTerm(value='deity_042', title=_(u'SanQingDZ')),
            SimpleTerm(value='deity_043', title=_(u'SanBaoFZ')),
            SimpleTerm(value='deity_044', title=_(u'XiaYuanDD')),
            SimpleTerm(value='deity_045', title=_(u'QianShouGY')),
            SimpleTerm(value='deity_046', title=_(u'DaShiYe')),
            SimpleTerm(value='deity_047', title=_(u'DaRiRuLai')),
            SimpleTerm(value='deity_048', title=_(u'NuGuoNN')),
            SimpleTerm(value='deity_049', title=_(u'WuGongZS')),
            SimpleTerm(value='deity_050', title=_(u'WuWenChang')),
            SimpleTerm(value='deity_051', title=_(u'WuLuCaiShen')),
            SimpleTerm(value='deity_052', title=_(u'WuFuDD')),
            SimpleTerm(value='deity_053', title=_(u'WuYueDD')),
            SimpleTerm(value='deity_054', title=_(u'WuXianDD')),
            SimpleTerm(value='deity_055', title=_(u'WuXianLG')),
            SimpleTerm(value='deity_056', title=_(u'YuanShiTZ')),
            SimpleTerm(value='deity_057', title=_(u'TianGuanDD')),
            SimpleTerm(value='deity_058', title=_(u'TianQianWD')),
            SimpleTerm(value='deity_059', title=_(u'TaiYiTZ')),
            SimpleTerm(value='deity_060', title=_(u'TaiShangLJ')),
            SimpleTerm(value='deity_061', title=_(u'TaiBaiJX')),
            SimpleTerm(value='deity_062', title=_(u'TaiBaiSJ')),
            SimpleTerm(value='deity_063', title=_(u'TaiYinXJ')),
            SimpleTerm(value='deity_064', title=_(u'TaiYangXJ')),
            SimpleTerm(value='deity_065', title=_(u'KongZi')),
            SimpleTerm(value='deity_066', title=_(u'KongMing')),
            SimpleTerm(value='deity_067', title=_(u'WenChangDJ')),
            SimpleTerm(value='deity_068', title=_(u'RiYueEDS')),
            SimpleTerm(value='deity_069', title=_(u'ShueiXianW')),
            SimpleTerm(value='deity_070', title=_(u'ShueiDeXJ')),
            SimpleTerm(value='deity_071', title=_(u'WangTianJ')),
            SimpleTerm(value='deity_072', title=_(u'WangFen')),
            SimpleTerm(value='deity_073', title=_(u'WnagChanLZ')),
            SimpleTerm(value='deity_074', title=_(u'BaoZheng')),
            SimpleTerm(value='deity_075', title=_(u'BeiYueDD')),
            SimpleTerm(value='deity_076', title=_(u'GuGongSW')),
            SimpleTerm(value='deity_077', title=_(u'LuBanG')),
            SimpleTerm(value='deity_078', title=_(u'ZhaoGongMing')),
            SimpleTerm(value='deity_079', title=_(u'YuErSM')),
            SimpleTerm(value='deity_080', title=_(u'TianDuYS')),
            SimpleTerm(value='deity_081', title=_(u'WnagShenZhi')),
            SimpleTerm(value='deity_082', title=_(u'ZhongKuei')),
            SimpleTerm(value='deity_083', title=_(u'LiGuanTao')),
            SimpleTerm(value='deity_084', title=_(u'DiMuNN')),
            SimpleTerm(value='deity_085', title=_(u'DiJiZhu')),
            SimpleTerm(value='deity_086', title=_(u'DiZhangWang')),
            SimpleTerm(value='deity_087', title=_(u'XiQinWang')),
            SimpleTerm(value='deity_088', title=_(u'XiYueDD')),
            SimpleTerm(value='deity_089', title=_(u'HeQiong')),
            SimpleTerm(value='deity_090', title=_(u'JiaLanZW')),
            SimpleTerm(value='deity_091', title=_(u'HuangDaoZhou')),
            SimpleTerm(value='deity_092', title=_(u'WuFengG')),
            SimpleTerm(value='deity_093', title=_(u'LiJingW')),
            SimpleTerm(value='deity_094', title=_(u'LiTieGuai')),
            SimpleTerm(value='deity_095', title=_(u'ZhouCang')),
            SimpleTerm(value='deity_096', title=_(u'MengChang')),
            SimpleTerm(value='deity_097', title=_(u'DingGuangFZ')),
            SimpleTerm(value='deity_098', title=_(u'YueFeiW')),
            SimpleTerm(value='deity_099', title=_(u'ChenYong')),
            SimpleTerm(value='deity_100', title=_(u'MingMingSD')),
            SimpleTerm(value='deity_101', title=_(u'DongHuaDJ')),
            SimpleTerm(value='deity_102', title=_(u'DongYueDD')),
            SimpleTerm(value='deity_103', title=_(u'ShenBiao')),
            SimpleTerm(value='deity_104', title=_(u'ZhangFZG')),
            SimpleTerm(value='deity_105', title=_(u'HuYeG')),
            SimpleTerm(value='deity_106', title=_(u'JinZhaYS')),
            SimpleTerm(value='deity_107', title=_(u'AMiTuoFo')),
            SimpleTerm(value='deity_108', title=_(u'NanJiXW')),
            SimpleTerm(value='deity_109', title=_(u'JiangZiYa')),
            SimpleTerm(value='deity_110', title=_(u'SuenBin')),
            SimpleTerm(value='deity_111', title=_(u'XuanYuanHD')),
            SimpleTerm(value='deity_112', title=_(u'KangZhaoYS')),
            SimpleTerm(value='deity_113', title=_(u'ZhangJinHua')),
            SimpleTerm(value='deity_114', title=_(u'ZhangTS')),
            SimpleTerm(value='deity_115', title=_(u'HeYeXS')),
            SimpleTerm(value='deity_116', title=_(u'GuoZiYi')),
            SimpleTerm(value='deity_117', title=_(u'HanDanYe')),
            SimpleTerm(value='deity_118', title=_(u'PuDuGong')),
            SimpleTerm(value='deity_119', title=_(u'PuAnFZ')),
            SimpleTerm(value='deity_120', title=_(u'BeiJiDD')),
            SimpleTerm(value='deity_121', title=_(u'JinPuFR')),
            SimpleTerm(value='deity_122', title=_(u'ZhuShengNN')),
            SimpleTerm(value='deity_123', title=_(u'ChenYuan')),
            SimpleTerm(value='deity_124', title=_(u'WuShaG')),
            SimpleTerm(value='deity_125', title=_(u'XiangYuYS')),
            SimpleTerm(value='deity_126', title=_(u'XuXun')),
            SimpleTerm(value='deity_127', title=_(u'YangYanDe')),
            SimpleTerm(value='deity_128', title=_(u'YangGongBS')),
            SimpleTerm(value='deity_129', title=_(u'YangFLSG')),
            SimpleTerm(value='deity_130', title=_(u'YangFTS')),
            SimpleTerm(value='deity_131', title=_(u'ZhuenTiPS')),
            SimpleTerm(value='deity_132', title=_(u'YiMingXY')),
            SimpleTerm(value='deity_133', title=_(u'DongGong')),
            SimpleTerm(value='deity_134', title=_(u'DaMoZS')),
            SimpleTerm(value='deity_135', title=_(u'JingZhuZW')),
            SimpleTerm(value='deity_136', title=_(u'BiXiaYJ')),
            SimpleTerm(value='deity_137', title=_(u'ZhaoZiLong')),
            SimpleTerm(value='deity_138', title=_(u'LiBoMiao')),
            SimpleTerm(value='deity_139', title=_(u'MaRenG')),
            SimpleTerm(value='deity_140', title=_(u'MaXFSJJ')),
            SimpleTerm(value='deity_141', title=_(u'KueiXinFZ')),
            SimpleTerm(value='deity_142', title=_(u'QiTianDS')),
            SimpleTerm(value='deity_143', title=_(u'DiTianDD')),
            SimpleTerm(value='deity_144', title=_(u'PanGuZS')),
            SimpleTerm(value='deity_145', title=_(u'ZhangLSFZ')),
            SimpleTerm(value='deity_146', title=_(u'LongDeXJ')),
            SimpleTerm(value='deity_147', title=_(u'LongShuZW')),
            SimpleTerm(value='deity_148', title=_(u'MiLeFZ')),
            SimpleTerm(value='deity_149', title=_(u'HanChangLi')),
            SimpleTerm(value='deity_150', title=_(u'HongJunLZ')),
            SimpleTerm(value='deity_151', title=_(u'QueGongZR')),
            SimpleTerm(value='deity_152', title=_(u'YaoWangDD')),
            SimpleTerm(value='deity_153', title=_(u'YaoShiFo')),
            SimpleTerm(value='deity_154', title=_(u'LuGongXS')),
            SimpleTerm(value='deity_155', title=_(u'ShiJiaMoNiF')),
            SimpleTerm(value='deity_156', title=_(u'FuGuoZW')),
            SimpleTerm(value='deity_157', title=_(u'FengDuDD')),
            SimpleTerm(value='deity_158', title=_(u'XianYingZS')),
            SimpleTerm(value='deity_159', title=_(u'LingAnZW')),
            SimpleTerm(value='deity_160', title=_(u'LingBaoTZ')),
            SimpleTerm(value='deity_161', title=_(u'LiShanLM')),
            SimpleTerm(value='deity_162', title=_(u'DaYuDW')),
            SimpleTerm(value='deity_163', title=_(u'ZhangXuEYS')),
            SimpleTerm(value='deity_164', title=_(u'WenShuPS')),
            SimpleTerm(value='deity_165', title=_(u'WenCaiShen')),
            SimpleTerm(value='deity_166', title=_(u'DouLaoYJ')),
            SimpleTerm(value='deity_167', title=_(u'BeiDouXJ')),
            SimpleTerm(value='deity_168', title=_(u'SiMianFo')),
            SimpleTerm(value='deity_169', title=_(u'XuanZhangDS')),
            SimpleTerm(value='deity_170', title=_(u'ZhuYiGuei')),
            SimpleTerm(value='deity_171', title=_(u'ZhuXiG')),
            SimpleTerm(value='deity_172', title=_(u'XiFangSS')),
            SimpleTerm(value='deity_173', title=_(u'LuDongBin')),
            SimpleTerm(value='deity_174', title=_(u'ZhaoKuangYing')),
            SimpleTerm(value='deity_175', title=_(u'LiGuangQian')),
            SimpleTerm(value='deity_176', title=_(u'ALiZhu')),
            SimpleTerm(value='deity_177', title=_(u'NanYueSH')),
            SimpleTerm(value='deity_178', title=_(u'ChenWeiWu')),
            SimpleTerm(value='deity_179', title=_(u'LiouXJ')),
            SimpleTerm(value='deity_180', title=_(u'HuangLingDZ')),
            SimpleTerm(value='deity_181', title=_(u'WeiTuoPS')),
            SimpleTerm(value='deity_182', title=_(u'FeiTianDS')),
            SimpleTerm(value='deity_183', title=_(u'EnZhuXY')),
            SimpleTerm(value='deity_184', title=_(u'CaiShenYe')),
            SimpleTerm(value='deity_185', title=_(u'KangMiaoWei')),
            SimpleTerm(value='deity_186', title=_(u'YinYangG')),
            SimpleTerm(value='deity_187', title=_(u'PuXianPS')),
            SimpleTerm(value='deity_188', title=_(u'WuLiangYSWF')),
            SimpleTerm(value='deity_189', title=_(u'WuJiLaoMuNN')),
            SimpleTerm(value='deity_190', title=_(u'WuJiSZ')),
            SimpleTerm(value='deity_191', title=_(u'HuaTuoS')),
            SimpleTerm(value='deity_192', title=_(u'JieZhiTuei')),
            SimpleTerm(value='deity_193', title=_(u'ShuenZhengDW')),
            SimpleTerm(value='deity_194', title=_(u'YuanTongZZTZ')),
            SimpleTerm(value='deity_195', title=_(u'ShenJunXY')),
            SimpleTerm(value='deity_196', title=_(u'ShuShenXY')),
            SimpleTerm(value='deity_197', title=_(u'LeiWanChuen')),
        )
        return SimpleVocabulary(items)
deity_nameFactory = deity_name()

class religion(object):
    """ Religion Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=_(u'rl_bd', default=u'Buddhism')),
            SimpleTerm(value='taoism', title=_(u'rl_to', default=u'Taoism')),
            SimpleTerm(value='confucianism', title=_(u'rl_cf', default=u'Confucianism')),
            SimpleTerm(value='liism', title=_(u'rl_li', default=u'Liism')),
            SimpleTerm(value='ikuantao', title=_(u'rl_ik', default=u'IKuanTao')),
            SimpleTerm(value='tienti', title=_(u'rl_tt', default=u'TienTi')),
            SimpleTerm(value='tenrikyo', title=_(u'rl_tr', default=u'TenRiKyo')),
            SimpleTerm(value='syuanyuanjiao', title=_(u'rl_sy', default=u'SyuanYuanJiao')),
            SimpleTerm(value='other', title=_(u'rl_ot', default=u'Other')),
        )
        return SimpleVocabulary(items)
religionFactory = religion()

class building(object):
    """ Building Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=_(u'bd_bd', default=u'Buddhism')),
            SimpleTerm(value='folk', title=_(u'bd_fk', default=u'Folk')),
            SimpleTerm(value='ikuantao', title=_(u'bd_ik', default=u'IKuanTao')),
            SimpleTerm(value='private', title=_(u'bd_pv', default=u'Private')),
            SimpleTerm(value='vegetarianhall', title=_(u'bd_vh', default=u'VegetarianHall')),
            SimpleTerm(value='phoenixhall', title=_(u'bd_ph', default=u'PhoenixHall')),
            SimpleTerm(value='taoism', title=_(u'bd_to', default=u'Taoism')),
            SimpleTerm(value='other', title=_(u'bd_ot', default=u'Other')),
        )
        return SimpleVocabulary(items)
buildingFactory = building()

class funding(object):
    """ Funding Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='raising', title=_(u'Raising')),
            SimpleTerm(value='private', title=_(u'Private')),
            SimpleTerm(value='public', title=_(u'Public')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
fundingFactory = funding()

class organizing(object):
    """ Organizing Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='person', title=_(u'Person')),
            SimpleTerm(value='committee', title=_(u'Committee')),
            SimpleTerm(value='foundation', title=_(u'Foundation')),
            SimpleTerm(value='deacon', title=_(u'Deacon')),
            SimpleTerm(value='government', title=_(u'Government')),
            SimpleTerm(value='other', title=_(u'Other')),
        )
        return SimpleVocabulary(items)
organizingFactory = organizing()

class jstq(object):
    """ JiSiZuQun
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='jstq10', title=_(u'jstq10', default=u'QZ')),
            SimpleTerm(value='jstq11', title=_(u'jstq11', default=u'QZ SY')),
            SimpleTerm(value='jstq12', title=_(u'jstq12', default=u'QZ TA')),
            SimpleTerm(value='jstq13', title=_(u'jstq13', default=u'QZ AX')),
            SimpleTerm(value='jstq20', title=_(u'jstq20', default=u'ZZ')),
            SimpleTerm(value='jstq21', title=_(u'jstq21', default=u'ZZ FL')),
            SimpleTerm(value='jstq22', title=_(u'jstq22', default=u'ZZ KJ')),
            SimpleTerm(value='jstq30', title=_(u'jstq30', default=u'GD')),
            SimpleTerm(value='jstq31', title=_(u'jstq31', default=u'GD CZ')),
            SimpleTerm(value='jstq32', title=_(u'jstq32', default=u'GD JY')),
            SimpleTerm(value='jstq33', title=_(u'jstq33', default=u'GD HZ')),
            SimpleTerm(value='jstq34', title=_(u'jstq34', default=u'GD FL')),
            SimpleTerm(value='jstq41', title=_(u'jstq41', default=u'OT PPZ')),
            SimpleTerm(value='jstq42', title=_(u'jstq42', default=u'OT DZK')),
            SimpleTerm(value='jstq43', title=_(u'jstq43', default=u'OT ZHYM')),
        )
        return SimpleVocabulary(items)
jstqFactory = jstq()

class flxt(object):
    """ FenLingXiTong
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='flxt10', title=_(u'flxt10', default=u'MZ')),
            SimpleTerm(value='flxt11', title=_(u'flxt11', default=u'MZ BGC')),
            SimpleTerm(value='flxt12', title=_(u'flxt12', default=u'MZ XGF')),
            SimpleTerm(value='flxt13', title=_(u'flxt13', default=u'MZ LGT')),
            SimpleTerm(value='flxt14', title=_(u'flxt14', default=u'MZ GDT')),
            SimpleTerm(value='flxt15', title=_(u'flxt15', default=u'MZ ZLG')),
            SimpleTerm(value='flxt16', title=_(u'flxt16', default=u'MZ NYG')),
            SimpleTerm(value='flxt17', title=_(u'flxt17', default=u'MZ YCL')),
            SimpleTerm(value='flxt18', title=_(u'flxt18', default=u'MZ TND')),
            SimpleTerm(value='flxt19', title=_(u'flxt19', default=u'MZ PTG')),
            SimpleTerm(value='flxt20', title=_(u'flxt20', default=u'MZ GKG')),
            SimpleTerm(value='flxt21', title=_(u'flxt21', default=u'MZ TAG')),
            SimpleTerm(value='flxt22', title=_(u'flxt22', default=u'MZ OT')),
            SimpleTerm(value='flxt30', title=_(u'flxt30', default=u'WY')),
            SimpleTerm(value='flxt31', title=_(u'flxt31', default=u'WY NKS')),
            SimpleTerm(value='flxt32', title=_(u'flxt32', default=u'WY MAD')),
            SimpleTerm(value='flxt33', title=_(u'flxt33', default=u'WY DLG')),
            SimpleTerm(value='flxt34', title=_(u'flxt34', default=u'WY MMS')),
            SimpleTerm(value='flxt35', title=_(u'flxt35', default=u'WY AXF')),
            SimpleTerm(value='flxt36', title=_(u'flxt36', default=u'WY GST')),
            SimpleTerm(value='flxt37', title=_(u'flxt37', default=u'WY BOX')),
            SimpleTerm(value='flxt38', title=_(u'flxt38', default=u'WY LGG')),
            SimpleTerm(value='flxt39', title=_(u'flxt39', default=u'WY FSG')),
            SimpleTerm(value='flxt40', title=_(u'flxt40', default=u'WY OT')),
            SimpleTerm(value='flxt41', title=_(u'flxt41', default=u'WY BHG')),
            SimpleTerm(value='flxt50', title=_(u'flxt50', default=u'GY')),
            SimpleTerm(value='flxt51', title=_(u'flxt51', default=u'GY LSS')),
            SimpleTerm(value='flxt52', title=_(u'flxt52', default=u'GY CFS')),
            SimpleTerm(value='flxt53', title=_(u'flxt53', default=u'GY LHY')),
            SimpleTerm(value='flxt54', title=_(u'flxt54', default=u'GY BYS')),
            SimpleTerm(value='flxt55', title=_(u'flxt55', default=u'GY DXS')),
            SimpleTerm(value='flxt56', title=_(u'flxt56', default=u'GY ZZS')),
            SimpleTerm(value='flxt57', title=_(u'flxt57', default=u'GY ZYS')),
            SimpleTerm(value='flxt58', title=_(u'flxt58', default=u'GY ZYY')),
            SimpleTerm(value='flxt59', title=_(u'flxt59', default=u'GY QSY')),
            SimpleTerm(value='flxt60', title=_(u'flxt60', default=u'GY OT')),
            SimpleTerm(value='flxt81', title=_(u'flxt81', default=u'WM SAG')),
            SimpleTerm(value='flxt82', title=_(u'flxt82', default=u'WM CHT')),
            SimpleTerm(value='flxt70', title=_(u'flxt70', default=u'OT')),
            SimpleTerm(value='flxt71', title=_(u'flxt71', default=u'OT GZXL')),
            SimpleTerm(value='flxt72', title=_(u'flxt72', default=u'OT GZYH')),
            SimpleTerm(value='flxt73', title=_(u'flxt73', default=u'OT XTSB')),
            SimpleTerm(value='flxt74', title=_(u'flxt74', default=u'OT XTWD')),
            SimpleTerm(value='flxt75', title=_(u'flxt75', default=u'OT BSDD')),
            SimpleTerm(value='flxt76', title=_(u'flxt76', default=u'OT ZTYS')),
            SimpleTerm(value='flxt77', title=_(u'flxt77', default=u'OT SSGW')),
        )
        return SimpleVocabulary(items)
flxtFactory = flxt()

class ymmy(object):
    """ YiMingMiaoYu
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='ymmy01', title=_(u'ymmy01', default=u'PHM')),
            SimpleTerm(value='ymmy02', title=_(u'ymmy02', default=u'DCM')),
            SimpleTerm(value='ymmy03', title=_(u'ymmy03', default=u'APM')),
            SimpleTerm(value='ymmy04', title=_(u'ymmy04', default=u'DSM')),
        )
        return SimpleVocabulary(items)
ymmyFactory = ymmy()

class xhly(object):
    """ XiangHuoLaiYuan
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='xhly01', title=_(u'xhly01', default=u'ZX')),
            SimpleTerm(value='xhly02', title=_(u'xhly02', default=u'XH')),
            SimpleTerm(value='xhly03', title=_(u'xhly03', default=u'BK')),
            SimpleTerm(value='xhly04', title=_(u'xhly04', default=u'SM')),
            SimpleTerm(value='xhly05', title=_(u'xhly05', default=u'WC')),
            SimpleTerm(value='xhly06', title=_(u'xhly06', default=u'NS')),
            SimpleTerm(value='xhly07', title=_(u'xhly07', default=u'FL')),
            SimpleTerm(value='xhly08', title=_(u'xhly08', default=u'ZS')),
            SimpleTerm(value='xhly09', title=_(u'xhly09', default=u'AZ')),
        )
        return SimpleVocabulary(items)
xhlyFactory = xhly()

class nlqs(object):
    """ NianLiQingShen
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='nlqs01', title=_(u'nlqs01', default=u'GDMZ')),
            SimpleTerm(value='nlqs02', title=_(u'nlqs02', default=u'BGMZ')),
            SimpleTerm(value='nlqs03', title=_(u'nlqs03', default=u'XGMZ')),
            SimpleTerm(value='nlqs04', title=_(u'nlqs04', default=u'ZHMZ')),
            SimpleTerm(value='nlqs05', title=_(u'nlqs05', default=u'WNQS')),
        )
        return SimpleVocabulary(items)
nlqsFactory = nlqs()

class wyxx(object):
    """ WangYeXianXiang
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='wyxx01', title=_(u'wyxx01', default=u'SC')),
            SimpleTerm(value='wyxx02', title=_(u'wyxx02', default=u'QWF')),
            SimpleTerm(value='wyxx03', title=_(u'wyxx03', default=u'QWN')),
            SimpleTerm(value='wyxx04', title=_(u'wyxx04', default=u'WCF')),
            SimpleTerm(value='wyxx05', title=_(u'wyxx05', default=u'WCN')),
            SimpleTerm(value='wyxx06', title=_(u'wyxx06', default=u'WJ')),
            SimpleTerm(value='wyxx07', title=_(u'wyxx07', default=u'OT')),
        )
        return SimpleVocabulary(items)
wyxxFactory = wyxx()

class medicine(object):
    """ Medicine Divination
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='medicine00', title=_(u'medicine00', default=u'NO')),
            SimpleTerm(value='medicine01', title=_(u'medicine01', default=u'DR')),
            SimpleTerm(value='medicine02', title=_(u'medicine02', default=u'XE')),
            SimpleTerm(value='medicine03', title=_(u'medicine03', default=u'FK')),
            SimpleTerm(value='medicine04', title=_(u'medicine04', default=u'YK')),
            SimpleTerm(value='medicine05', title=_(u'medicine05', default=u'OT')),
        )
        return SimpleVocabulary(items)
medicineFactory = medicine()

class luck(object):
    """ Luck Divination
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='luck00', title=_(u'luck00', default=u'NO')),
            SimpleTerm(value='luck01', title=_(u'luck01', default=u'ST')),
            SimpleTerm(value='luck02', title=_(u'luck02', default=u'HD')),
            SimpleTerm(value='luck03', title=_(u'luck03', default=u'OT')),
        )
        return SimpleVocabulary(items)
luckFactory = luck()

class bixiewu(object):
    """ BiXieWu Types
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='ShiGanDang', title=_(u'ShiGanDang')),
            SimpleTerm(value='FengShiYe', title=_(u'FengShiYe')),
            SimpleTerm(value='ShenXiang', title=_(u'ShenXiang')),
            SimpleTerm(value='BeiWenFuZhou', title=_(u'BeiWenFuZhou')),
            SimpleTerm(value='Ta', title=_(u'Ta')),
            SimpleTerm(value='JianShi', title=_(u'JianShi')),
            SimpleTerm(value='ShanHaiZhen', title=_(u'ShanHaiZhen')),
            SimpleTerm(value='BaGua', title=_(u'BaGua')),
            SimpleTerm(value='QiWu', title=_(u'QiWu')),
            SimpleTerm(value='ZhaoBi', title=_(u'ZhaoBi')),
            SimpleTerm(value='ShenShou', title=_(u'ShenShou')),
            SimpleTerm(value='ZhiWu', title=_(u'ZhiWu')),
            SimpleTerm(value='other', title=_(u'other')),
        )
        return SimpleVocabulary(items)
bixiewuFactory = bixiewu()

class material(object):
    """ Material
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='stone', title=_(u'stone')),
            SimpleTerm(value='mud', title=_(u'mud')),
            SimpleTerm(value='coment', title=_(u'coment')),
            SimpleTerm(value='brick', title=_(u'brick')),
            SimpleTerm(value='ceramics', title=_(u'ceramics')),
            SimpleTerm(value='wood', title=_(u'wood')),
            SimpleTerm(value='other', title=_(u'other')),
        )
        return SimpleVocabulary(items)
materialFactory = material()

class locational(object):
    """ Locational Attribute
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='JuLuo', title=_(u'JuLuo')),
            SimpleTerm(value='LuKuo', title=_(u'LuKuo')),
            SimpleTerm(value='SiRen', title=_(u'SiRen')),
            SimpleTerm(value='other', title=_(u'other')),
        )
        return SimpleVocabulary(items)
locationalFactory = locational()

class purpose(object):
    """ Purpose
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='JuLuoZhenSha', title=_(u'JuLuoZhenSha')),
            SimpleTerm(value='AnZhenLuKou', title=_(u'AnZhenLuKou')),
            SimpleTerm(value='LuChong', title=_(u'LuChong')),
            SimpleTerm(value='ZhenFeng', title=_(u'ZhenFeng')),
            SimpleTerm(value='ZhenShui', title=_(u'ZhenShui')),
            SimpleTerm(value='FenMu', title=_(u'FenMu')),
            SimpleTerm(value='HaiBian', title=_(u'HaiBian')),
            SimpleTerm(value='WuChong', title=_(u'WuChong')),
        )
        return SimpleVocabulary(items)
purposeFactory = purpose()

class isExisting(object):
    """ isExisting
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='yes', title=_(u'yes')),
            SimpleTerm(value='no', title=_(u'no')),
        )
        return SimpleVocabulary(items)
isExistingFactory = isExisting()

class genre(object):
    """ genre
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='village', title=_(u'village')),
            SimpleTerm(value='wall', title=_(u'wall')),
            SimpleTerm(value='roof', title=_(u'roof')),
        )
        return SimpleVocabulary(items)
genreFactory = genre()

class posture(object):
    """ posture
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='standing', title=_(u'standing')),
            SimpleTerm(value='crouching', title=_(u'crouching')),
            SimpleTerm(value='lying', title=_(u'lying')),
            SimpleTerm(value='sitting', title=_(u'sitting')),
            SimpleTerm(value='reclining', title=_(u'reclining')),
        )
        return SimpleVocabulary(items)
postureFactory = posture()

class gender(object):
    """ gender
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='male', title=_(u'male')),
            SimpleTerm(value='female', title=_(u'female')),
            SimpleTerm(value='unknown', title=_(u'unknown')),
        )
        return SimpleVocabulary(items)
genderFactory = gender()

class category(object):
    """ category
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='temple', title=_(u'TemPle')),
            SimpleTerm(value='bixiewu', title=_(u'BiXieWu')),
            SimpleTerm(value='wuying', title=_(u'WyYing')),
        )
        return SimpleVocabulary(items)
categoryFactory = category()

class year_accuracy(object):
    """ year_accuracy
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='exact', title=_(u'Exact')),
            SimpleTerm(value='fuzzy', title=_(u'Fuzzy')),
            SimpleTerm(value='unknown', title=_(u'Unknown')),
        )
        return SimpleVocabulary(items)
yearAccuracyFactory = year_accuracy()

class attachesTo(object):
    """ attachesTo
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='history', title=_(u'Establishment History')),
            SimpleTerm(value='worship', title=_(u'Worship')),
            SimpleTerm(value='introduction', title=_(u'Introduction')),
            SimpleTerm(value='overview', title=_(u'Building Overview')),
            SimpleTerm(value='antiquity', title=_(u'Antiquities')),
            SimpleTerm(value='narrate', title=_(u'Narrate')),
            SimpleTerm(value='non_narrate', title=_(u'Non Narrate')),
            SimpleTerm(value='spatial', title=_(u'Spatial Attribute')),
        )
        return SimpleVocabulary(items)
attachesToFactory = attachesTo()

