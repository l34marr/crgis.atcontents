#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from crgis.atcontents import atcontentsMessageFactory as _

def unicode_vocabulary(proplist):
    #return a Vocabulary with valid ascii Token and unicode Title and Value
    return [SimpleVocabulary.createTerm(
         safe_unicode(i),
         safe_unicode(i).encode('ascii', 'replace'),
         safe_unicode(i)) for i in proplist]

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
            SimpleTerm(value='deity_001', title=u'王爺，千歲，二府王爺，三府王爺，四府王爺，四府千歲，五府千歲，十二瘟王，刑府千歲，池王爺，池府千歲，丁府八千歲，蕭府王爺，蕭太傅，朱李池三府王爺，朱李池吳范五府，代天巡狩，各姓王爺，各府王爺'),
            SimpleTerm(value='deity_002', title=u'城隍，城隍爺，城隍老爺，都城隍，省城隍，縣城隍，安溪城隍，霞海城隍'),
            SimpleTerm(value='deity_003', title=u'土地公，福德，福德正神，福德老爺，伯公，土地正神，土地伯公'),
            SimpleTerm(value='deity_004', title=u'陰神 (大將爺，大眾爺，大眾公，大眾媽，百姓公，有應公，老大公，泉州公，陰公，萬姓公，萬姓媽，萬善爺，萬善公，十八王公，三善公，三姑娘，三姓公，冥應公，冥漠公，千眾爺，好漢公)'),
            SimpleTerm(value='deity_005', title=u'天上聖母，媽祖，湄洲聖母'),
            SimpleTerm(value='deity_006', title=u'中壇元帥，三太子，太子爺，哪吒太子，哪吒三太子，中壇太子，中壇太子元帥，那吒'),
            SimpleTerm(value='deity_007', title=u'保生大帝，吳真人，吳真君，吳公真仙，真人仙師，大道公，保生二大帝，保生上帝'),
            SimpleTerm(value='deity_008', title=u'玄天上帝，上帝爺，上帝爺公，上帝公，北極玄天上帝，北極玄天二帝，北極大帝，北極上帝，北方真武上帝，北極真武老祖，真武大帝，玄天大帝，玄天真武大帝，帝爺公'),
            SimpleTerm(value='deity_009', title=u'五穀仙帝，神農大帝，神農聖帝，神農帝書，五榖王，五穀先帝，五穀大帝，五穀聖帝，五穀神農，五穀爺，五谷仙帝，五谷先帝，五谷大帝，五谷聖帝，五谷神農皇帝，開天炎帝，開天仙帝'),
            SimpleTerm(value='deity_010', title=u'廣澤尊王，保安尊王，保安廣澤尊王，聖王公，郭府聖王，廣澤尊神'),
            SimpleTerm(value='deity_011', title=u'關聖帝君，關公，關羽，關雲長，關帝爺，關二爺，山西夫子，文衡聖帝，文衡聖君，文衡帝君，伏魔大帝，南天聖帝，協天大帝，協天上帝，協天聖帝，恩主公'),
            SimpleTerm(value='deity_012', title=u'觀世音菩薩，觀世音，觀世大士，觀音，觀音媽，觀音菩薩，觀音大士，觀音佛祖，南海佛祖，南海觀世音菩薩，南無觀世音菩薩，佛祖媽，正法明如來'),
            SimpleTerm(value='deity_013', title=u'玉皇大帝，玉皇大帝，玉皇大天尊，昊天大帝，金闕大帝，玄天靈高上帝'),
            SimpleTerm(value='deity_014', title=u'王母娘娘，瑤池金母，瑤池聖母，西方瑤池金母，西王金母，西王聖母，金母娘娘，西王國母娘娘'),
            SimpleTerm(value='deity_015', title=u'三官大帝，三元三品三官大帝，三界公，三官天帝'),
            SimpleTerm(value='deity_016', title=u'三奶夫人，三奶夫人媽，陳林李三奶夫人'),
            SimpleTerm(value='deity_017', title=u'臨水夫人，陳靖姑，陳奶夫人，陳乃夫人，夫人媽，順天聖母，臨水陳太后，靖姑娘媽，福州聖母'),
            SimpleTerm(value='deity_018', title=u'鄭成功，開台國聖，開臺聖王，開台聖王，開台尊王，開山王國姓公，國姓公，延平郡王，國聖公，國聖爺，國姓爺'),
            SimpleTerm(value='deity_019', title=u'三山國王，三仙國王，三仙國王爺，開山聖王，明山國王'),
            SimpleTerm(value='deity_020', title=u'清水祖師，祖師公，三代祖師，蓬萊祖師，顯應祖師'),
            SimpleTerm(value='deity_021', title=u'慚愧祖師，蔭林祖師，蔭林慚愧祖師，陰林祖師'),
            SimpleTerm(value='deity_022', title=u'三坪祖師，三坪祖師公，三坪祖師爺，義中大師，廣濟禪師'),
            SimpleTerm(value='deity_023', title=u'九天玄女，九天娘娘'),
            SimpleTerm(value='deity_024', title=u'濟公禪師，濟公，濟公菩薩，濟公活佛，道濟仙師，道濟先師，道濟禪師，道濟古佛'),
            SimpleTerm(value='deity_025', title=u'開漳聖王，陳聖王，陳元光'),
            SimpleTerm(value='deity_026', title=u'張巡 (保儀大夫，保儀尊王，武安尊王，尪公)'),
            SimpleTerm(value='deity_027', title=u'許遠 (保儀尊王，保儀大夫，武安尊王，文安尊王，尪公)'),
            SimpleTerm(value='deity_028', title=u'鄭保惠 (保儀尊王)'),
            SimpleTerm(value='deity_029', title=u'謝安，廣惠聖王，謝府王公，謝千歲，謝聖王，謝王公，謝安王，謝老元帥，廣惠尊王，廣應聖王，廣應尊王，顯濟靈王，護國尊王'),
            SimpleTerm(value='deity_030', title=u'謝玄，謝府元帥，王孫大使，平南元帥，大使爺'),
            SimpleTerm(value='deity_031', title=u'七星娘娘，七娘媽'),
            SimpleTerm(value='deity_032', title=u'七祖仙師，七祖先師，黃仲仁'),
            SimpleTerm(value='deity_033', title=u'九天司命真君，司命灶君，司命真君，東廚帝君'),
            SimpleTerm(value='deity_034', title=u'九府仙師'),
            SimpleTerm(value='deity_035', title=u'九皇大帝'),
            SimpleTerm(value='deity_036', title=u'九蓮佛祖'),
            SimpleTerm(value='deity_037', title=u'九龍三公，九龍魏府三公爺'),
            SimpleTerm(value='deity_038', title=u'二郎神君，二郎尊神，楊戩'),
            SimpleTerm(value='deity_039', title=u'八卦祖師，伏羲氏，伏羲大帝，伏羲先帝，伏羲八卦祖師'),
            SimpleTerm(value='deity_040', title=u'十二延天溪女娘娘，十二廷女娘娘'),
            SimpleTerm(value='deity_041', title=u'三一教主，三教先生，林兆恩，林龍江'),
            SimpleTerm(value='deity_042', title=u'三清道祖，玉清元始天尊，上清靈寶天尊，太清道德天尊，三清祖師'),
            SimpleTerm(value='deity_043', title=u'三寶佛，三寶佛祖 (藥師佛、釋迦牟尼佛、阿彌陀佛)'),
            SimpleTerm(value='deity_044', title=u'下元水官大帝'),
            SimpleTerm(value='deity_045', title=u'千手觀音，千手千眼觀世音，千手觀音菩薩'),
            SimpleTerm(value='deity_046', title=u'大士爺'),
            SimpleTerm(value='deity_047', title=u'大日如來，摩訶毗盧遮那，大如天佛，盧舍那佛，思盧遮那佛，如來佛，摩訶昆盧遮那佛'),
            SimpleTerm(value='deity_048', title=u'女媧娘娘，女媧娘神'),
            SimpleTerm(value='deity_049', title=u'五公菩薩，五公禪師 (志公、化公、朗公、唐公、寶公)'),
            SimpleTerm(value='deity_050', title=u'五文昌帝君，五文昌夫子 (關聖帝君、魁斗星君、文昌帝君、純陽祖師、朱一神君)'),
            SimpleTerm(value='deity_051', title=u'五路財神，天宮五路武財神 (武財神趙公明、招財使者、進寶天尊、納珍天尊、利市仙官)'),
            SimpleTerm(value='deity_052', title=u'五福大帝，五靈公，五福天仙，五顯大帝'),
            SimpleTerm(value='deity_053', title=u'五嶽大帝'),
            SimpleTerm(value='deity_054', title=u'五顯大帝，五顯三大帝，宣靈公，宣靈公劉'),
            SimpleTerm(value='deity_055', title=u'五顯靈官，華光，華光大帝，五顯大帝，五顯靈官華光大帝'),
            SimpleTerm(value='deity_056', title=u'元始天尊，元始大天尊，太上元始天尊，無極至尊元始天王，元始天王'),
            SimpleTerm(value='deity_057', title=u'天官大帝'),
            SimpleTerm(value='deity_058', title=u'天僊伍帝，天遷五帝，天遷伍帝'),
            SimpleTerm(value='deity_059', title=u'太乙救苦天尊，救苦天尊，太乙真人'),
            SimpleTerm(value='deity_060', title=u'太上老君，太上李老君，太上道祖，道德天尊'),
            SimpleTerm(value='deity_061', title=u'太白金仙，太白金星'),
            SimpleTerm(value='deity_062', title=u'太白神君，李白'),
            SimpleTerm(value='deity_063', title=u'太陰星君，太陰娘娘'),
            SimpleTerm(value='deity_064', title=u'太陽星君，太陽公，太陽帝君，太陽神君，太陽星神'),
            SimpleTerm(value='deity_065', title=u'孔子，孔夫子，至聖先師'),
            SimpleTerm(value='deity_066', title=u'孔明先師，諸葛亮，諸葛孔明'),
            SimpleTerm(value='deity_067', title=u'文昌帝君，文昌公，梓潼帝君'),
            SimpleTerm(value='deity_068', title=u'日月二大使'),
            SimpleTerm(value='deity_069', title=u'水仙尊王，水仙王，水僊尊王'),
            SimpleTerm(value='deity_070', title=u'水德星君，水德聖君'),
            SimpleTerm(value='deity_071', title=u'王天君，王靈官，豁落靈官'),
            SimpleTerm(value='deity_072', title=u'王勳千歲，王分，王芬'),
            SimpleTerm(value='deity_073', title=u'王禪老祖，王禪老師，鬼谷子，鬼谷先生'),
            SimpleTerm(value='deity_074', title=u'包府千歲，包青天，包拯，包公，閰羅天子，包公尊主，包聖青天，包王爺'),
            SimpleTerm(value='deity_075', title=u'北嶽大帝'),
            SimpleTerm(value='deity_076', title=u'古公三王'),
            SimpleTerm(value='deity_077', title=u'巧聖仙師，魯班公，魯班先師，巧聖先師，巧聖先魯班公'),
            SimpleTerm(value='deity_078', title=u'玄壇元帥，武財神，趙公明，玄壇公，趙元帥，趙府元帥，元帥爺'),
            SimpleTerm(value='deity_079', title=u'玉二聖母'),
            SimpleTerm(value='deity_080', title=u'田都元帥，田府王爺，田府元帥'),
            SimpleTerm(value='deity_081', title=u'白馬尊王，王審之，白馬大王，白馬文武大王，開閩尊王'),
            SimpleTerm(value='deity_082', title=u'伏魔大帝，鍾馗，伏魔公，伏魔大將軍，鍾馗帝君，鍾馗爺爺'),
            SimpleTerm(value='deity_083', title=u'光耀大帝，李觀濤，濟世光耀大帝，金闕靈真官'),
            SimpleTerm(value='deity_084', title=u'地母至尊，地母，地母娘娘，地母尊神'),
            SimpleTerm(value='deity_085', title=u'地基主'),
            SimpleTerm(value='deity_086', title=u'地藏王菩薩，地藏王，地藏菩薩'),
            SimpleTerm(value='deity_087', title=u'西秦王爺，西秦王，公子爺，戲神'),
            SimpleTerm(value='deity_088', title=u'西嶽大帝，善璽，金天順聖帝，金天王，西嶽金天大帝'),
            SimpleTerm(value='deity_089', title=u'何仙姑，何瓊'),
            SimpleTerm(value='deity_090', title=u'伽藍尊王，伽藍尊神，伽藍千歲，伽藍爺'),
            SimpleTerm(value='deity_091', title=u'助順將軍，黃道周'),
            SimpleTerm(value='deity_092', title=u'吳鳳公，吳鳳'),
            SimpleTerm(value='deity_093', title=u'李天王，李靖，托塔天王，李靖托塔天王'),
            SimpleTerm(value='deity_094', title=u'李仙祖，李鐵拐，李鐵枴，凝陽帝君，凝陽祖師'),
            SimpleTerm(value='deity_095', title=u'周府將軍，周倉，周倉爺，周倉聖爺，周倉大將軍，周爺公，國聖爺'),
            SimpleTerm(value='deity_096', title=u'孟府郎君，孟昶，郎君大仙'),
            SimpleTerm(value='deity_097', title=u'定光古佛，定光佛祖'),
            SimpleTerm(value='deity_098', title=u'岳武穆王，岳飛，岳府千歲，元帥爺公，元帥爺，岳飛元帥，岳府王爺，岳府元帥'),
            SimpleTerm(value='deity_099', title=u'忠順聖王，忠順王，陳邕'),
            SimpleTerm(value='deity_100', title=u'明明上帝，無極老申明明上帝'),
            SimpleTerm(value='deity_101', title=u'東華帝君，東王木公，東王公'),
            SimpleTerm(value='deity_102', title=u'東嶽大帝，東嶽仁聖大帝，東嶽帝君，仁聖大帝'),
            SimpleTerm(value='deity_103', title=u'武德尊侯，沈彪，武德侯，武德英侯，輔美將軍，護國大將軍'),
            SimpleTerm(value='deity_104', title=u'法主公【張】，法主公聖君，法主聖君，張聖君，張公法主，張公聖君，代天法主，張聖真君'),
            SimpleTerm(value='deity_105', title=u'虎爺公，虎爺大將軍，虎爺，下壇將軍'),
            SimpleTerm(value='deity_106', title=u'金吒太子，金吒元帥'),
            SimpleTerm(value='deity_107', title=u'阿彌陀佛'),
            SimpleTerm(value='deity_108', title=u'南極仙翁'),
            SimpleTerm(value='deity_109', title=u'姜太公，姜子牙'),
            SimpleTerm(value='deity_110', title=u'孫臏真人，孫真人，孫臏祖師，孫臏仙師，孫府真人'),
            SimpleTerm(value='deity_111', title=u'軒轅黃帝，軒轅皇帝，黃帝，黃帝道祖，黃帝祖'),
            SimpleTerm(value='deity_112', title=u'康趙元帥 (康元帥，康妙威，仁聖元帥、趙元帥，趙公明)'),
            SimpleTerm(value='deity_113', title=u'張玉姑，張金花'),
            SimpleTerm(value='deity_114', title=u'張府天師，張天師，正一天師，廣信天師'),
            SimpleTerm(value='deity_115', title=u'荷葉仙師，芋葉仙師'),
            SimpleTerm(value='deity_116', title=u'郭子儀，郭令公，汾陽王，汾陽郡王'),
            SimpleTerm(value='deity_117', title=u'寒單爺'),
            SimpleTerm(value='deity_118', title=u'普度公，普渡公，中元普渡公'),
            SimpleTerm(value='deity_119', title=u'普庵祖佛，普庵佛祖，普庵真人，普庵祖師，普唵佛祖.普唵祖師'),
            SimpleTerm(value='deity_120', title=u'紫微大帝，北極大帝'),
            SimpleTerm(value='deity_121', title=u'菁埔夫人'),
            SimpleTerm(value='deity_122', title=u'註生娘娘'),
            SimpleTerm(value='deity_123', title=u'開浯恩主，陳淵，牧馬侯，福佑聖侯，福佑恩主，聖侯恩主，恩主聖侯'),
            SimpleTerm(value='deity_124', title=u'開蘭吳沙公，吳沙'),
            SimpleTerm(value='deity_125', title=u'項羽元帥，項羽，西楚霸王'),
            SimpleTerm(value='deity_126', title=u'感天大帝，許遜，許真人，閭山法主許遜，許九郎'),
            SimpleTerm(value='deity_127', title=u'大德禪師，楊延德，五使公，楊五郎'),
            SimpleTerm(value='deity_128', title=u'楊公八使'),
            SimpleTerm(value='deity_129', title=u'楊府六使公，楊六郎，楊府六使，六使公，楊六使'),
            SimpleTerm(value='deity_130', title=u'楊府太師，楊府大師，楊令公'),
            SimpleTerm(value='deity_131', title=u'準提佛母，準提菩薩，大準提菩薩，南無準提菩薩，南無準提佛母菩薩，佛母準提王菩薩，準提王菩薩，准提菩薩'),
            SimpleTerm(value='deity_132', title=u'義民信仰，粵東褒忠義民神，褒忠義民爺，義民公，褒雄義民，忠義公，義勇爺，義善姑，義士爺，靖忠元帥，靖惠侯郭仁公，羅福星'),
            SimpleTerm(value='deity_133', title=u'董公真仙，董公，安溪董公真人'),
            SimpleTerm(value='deity_134', title=u'達摩祖師，達摩'),
            SimpleTerm(value='deity_135', title=u'境主尊王，境主爺'),
            SimpleTerm(value='deity_136', title=u'碧霞元君'),
            SimpleTerm(value='deity_137', title=u'趙子龍，趙府千歲，趙聖帝君，趙聖定遠帝君，子龍爺，趙府元歲'),
            SimpleTerm(value='deity_138', title=u'輔信王公，李伯苗，輔信將軍，輔信大王，護聖公'),
            SimpleTerm(value='deity_139', title=u'馬仁，輔順將軍，舍人公，馬使爺，馬公爺，馬舍公'),
            SimpleTerm(value='deity_140', title=u'馬恩，馬援，馬安，馬福，輔順將軍'),
            SimpleTerm(value='deity_141', title=u'魁星夫子'),
            SimpleTerm(value='deity_142', title=u'齊天大聖，齊天大聖爺'),
            SimpleTerm(value='deity_143', title=u'敵天大帝，林放公'),
            SimpleTerm(value='deity_144', title=u'盤古祖師，盤古公，盤古帝王，盤古開天祖，盤古聖帝，盤古萬歲，磐古聖帝，開天聖帝'),
            SimpleTerm(value='deity_145', title=u'閭山法主【張】，閭山張公法王，閭山三元張公法主聖君'),
            SimpleTerm(value='deity_146', title=u'龍德星君'),
            SimpleTerm(value='deity_147', title=u'龍樹尊王，龍樹尊王菩薩'),
            SimpleTerm(value='deity_148', title=u'彌勒佛祖，彌勒佛，彌勒如來，彌勒古佛，彌勒尊佛，彌勒菩薩，彌勒祖師，彌樂祖師'),
            SimpleTerm(value='deity_149', title=u'韓愈，韓昌黎'),
            SimpleTerm(value='deity_150', title=u'鴻鈞老祖，鴻鈞始祖'),
            SimpleTerm(value='deity_151', title=u'瞿公真人，溥護瞿公真人'),
            SimpleTerm(value='deity_152', title=u'藥王大帝'),
            SimpleTerm(value='deity_153', title=u'藥師佛，藥師琉璃光如來，藥師琉璃光佛，南無消災延壽藥'),
            SimpleTerm(value='deity_154', title=u'爐公先師'),
            SimpleTerm(value='deity_155', title=u'釋迦牟尼佛，釋迦，釋迦佛祖，釋迦如來，釋迦如來佛，釋迦牟尼，釋迦佛，佛祖，南無本師釋迦牟尼'),
            SimpleTerm(value='deity_156', title=u'護國尊王'),
            SimpleTerm(value='deity_157', title=u'酆都大帝，豐都大帝'),
            SimpleTerm(value='deity_158', title=u'顯應祖師，顯應祖師公'),
            SimpleTerm(value='deity_159', title=u'靈安尊王，武德侯，青山王'),
            SimpleTerm(value='deity_160', title=u'靈寶天尊'),
            SimpleTerm(value='deity_161', title=u'驪山老母，黎山老母，梨山老母'),
            SimpleTerm(value='deity_162', title=u'大禹，禹帝，大夏聖帝，大聖夏帝，平水天王'),
            SimpleTerm(value='deity_163', title=u'保儀大夫，保儀尊王，雙忠聖王，張許二元帥，武安尊二王，尪元帥，尊王公，張府厲王，張府厲王爺，張府尊王，文安尊王'),
            SimpleTerm(value='deity_164', title=u'文殊菩薩'),
            SimpleTerm(value='deity_165', title=u'文財神'),
            SimpleTerm(value='deity_166', title=u'斗姥元君，道姥天尊'),
            SimpleTerm(value='deity_167', title=u'北斗星君'),
            SimpleTerm(value='deity_168', title=u'四面佛，大梵天王，四面金剛佛'),
            SimpleTerm(value='deity_169', title=u'玄奘大師'),
            SimpleTerm(value='deity_170', title=u'朱一貴，朱公一貴'),
            SimpleTerm(value='deity_171', title=u'朱熹，朱子公'),
            SimpleTerm(value='deity_172', title=u'西方三聖，華嚴三聖，三聖大佛，西方三聖佛 (佛陀、文殊菩薩、普賢菩薩)'),
            SimpleTerm(value='deity_173', title=u'孚佑帝君，呂洞濱，呂仙祖，仙公，純陽祖師，文尼真佛，純陽帝君'),
            SimpleTerm(value='deity_174', title=u'宋太祖，趙匡胤，太祖公'),
            SimpleTerm(value='deity_175', title=u'李光前將軍，李光前'),
            SimpleTerm(value='deity_176', title=u'阿立祖，阿力祖，阿立母，老祖，太祖 (平埔信仰)'),
            SimpleTerm(value='deity_177', title=u'南嶽聖侯'),
            SimpleTerm(value='deity_178', title=u'威武陳將軍，威烈侯陳將軍，威武將軍，威烈侯'),
            SimpleTerm(value='deity_179', title=u'柳星君，柳帝君'),
            SimpleTerm(value='deity_180', title=u'皇靈地祇'),
            SimpleTerm(value='deity_181', title=u'韋馱菩薩'),
            SimpleTerm(value='deity_182', title=u'飛天大聖，飛天大帝'),
            SimpleTerm(value='deity_183', title=u'恩主信仰 (三恩主，三尊恩主，三聖恩主，五恩主)'),
            SimpleTerm(value='deity_184', title=u'財神，財神爺 (文財神，武財神)'),
            SimpleTerm(value='deity_185', title=u'康元帥，康府元帥，康妙威'),
            SimpleTerm(value='deity_186', title=u'陰陽公'),
            SimpleTerm(value='deity_187', title=u'普賢菩薩'),
            SimpleTerm(value='deity_188', title=u'無量音聲王佛'),
            SimpleTerm(value='deity_189', title=u'無極老母，無極老母娘娘，無極老中，無極皇媽，無極皇母娘娘，無極神母，無極王母，無極靈山王母娘娘'),
            SimpleTerm(value='deity_190', title=u'無極聖祖'),
            SimpleTerm(value='deity_191', title=u'華陀神醫，華陀仙師，華陀仙翁'),
            SimpleTerm(value='deity_192', title=u'開山聖侯，介之推，開山大帝，大伯公，大伯爺'),
            SimpleTerm(value='deity_193', title=u'順正大王，順正大王公，順正府大王公，順正輔大王公，順王爺，武惠尊王，護國武惠尊王'),
            SimpleTerm(value='deity_194', title=u'圓通自在天尊'),
            SimpleTerm(value='deity_195', title=u'聖君信仰 (張聖君，連聖君，劉聖君，蕭聖君)'),
            SimpleTerm(value='deity_196', title=u'樹神信仰 (樹王公，大樹公，仙樹爺公，松樹王，松樹尊王，松王，檨王，檨仔王，樟樹公，樟仙師)'),
            SimpleTerm(value='deity_197', title=u'騎虎尊王，雷萬春'),
        )
        return SimpleVocabulary(items)
deity_nameFactory = deity_name()

class religion(object):
    """ Religion Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=u'佛'),
            SimpleTerm(value='taoism', title=u'道'),
            SimpleTerm(value='confucianism', title=u'儒'),
            SimpleTerm(value='liism', title=u'理'),
            SimpleTerm(value='ikuantao', title=u'一貫道'),
            SimpleTerm(value='tienti', title=u'天帝教'),
            SimpleTerm(value='tenrikyo', title=u'天理教'),
            SimpleTerm(value='syuanyuanjiao', title=u'軒轅教'),
            SimpleTerm(value='other', title=u'其他'),
        )
        return SimpleVocabulary(items)
religionFactory = religion()

class building(object):
    """ Building Type
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='buddhism', title=u'佛教寺院'),
            SimpleTerm(value='folk', title=u'民間寺廟'),
            SimpleTerm(value='ikuantao', title=u'一貫道'),
            SimpleTerm(value='private', title=u'私人寺廟'),
            SimpleTerm(value='vegetarianhall', title=u'齋堂'),
            SimpleTerm(value='phoenixhall', title=u'鸞堂'),
            SimpleTerm(value='taoism', title=u'道教宮觀'),
            SimpleTerm(value='other', title=u'其他'),
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
            SimpleTerm(value=u'jstq10', title=u'泉州'),
            SimpleTerm(value=u'jstq11', title=u'泉州 三邑（晉江、南安、惠安）'),
            SimpleTerm(value=u'jstq12', title=u'泉州 同安'),
            SimpleTerm(value=u'jstq13', title=u'泉州 安溪'),
            SimpleTerm(value=u'jstq20', title=u'漳州'),
            SimpleTerm(value=u'jstq21', title=u'漳州 福佬'),
            SimpleTerm(value=u'jstq22', title=u'漳州 客家（詔安客）'),
            SimpleTerm(value=u'jstq30', title=u'廣東'),
            SimpleTerm(value=u'jstq31', title=u'廣東 潮州（大埔客、饒平客）'),
            SimpleTerm(value=u'jstq32', title=u'廣東 嘉應（四縣客）'),
            SimpleTerm(value=u'jstq33', title=u'廣東 惠州（海陸客）'),
            SimpleTerm(value=u'jstq34', title=u'廣東 福佬'),
            SimpleTerm(value=u'jstq41', title=u'其他 平埔族'),
            SimpleTerm(value=u'jstq42', title=u'其他 汀州客'),
            SimpleTerm(value=u'jstq43', title=u'其他 戰後移民（外省）'),
        )
        return SimpleVocabulary(items)
jstqFactory = jstq()

class flxt(object):
    """ FenLingXiTong
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'flxt10', title=u'媽祖'),
            SimpleTerm(value=u'flxt11', title=u'媽祖 北港朝天宮'),
            SimpleTerm(value=u'flxt12', title=u'媽祖 新港奉天宮'),
            SimpleTerm(value=u'flxt13', title=u'媽祖 鹿港天后宮'),
            SimpleTerm(value=u'flxt14', title=u'媽祖 關渡天后宮'),
            SimpleTerm(value=u'flxt15', title=u'媽祖 大甲鎮瀾宮'),
            SimpleTerm(value=u'flxt16', title=u'媽祖 彰化南瑤宮'),
            SimpleTerm(value=u'flxt17', title=u'媽祖 燕巢龍角寺天后宮'),
            SimpleTerm(value=u'flxt18', title=u'媽祖 台南大天后宮'),
            SimpleTerm(value=u'flxt19', title=u'媽祖 朴子配天宮'),
            SimpleTerm(value=u'flxt20', title=u'媽祖 東石港口宮'),
            SimpleTerm(value=u'flxt21', title=u'媽祖 後壁泰安宮'),
            SimpleTerm(value=u'flxt22', title=u'媽祖 其他'),
            SimpleTerm(value=u'flxt30', title=u'王爺'),
            SimpleTerm(value=u'flxt31', title=u'王爺 南鯤鯓代天府（五府）'),
            SimpleTerm(value=u'flxt32', title=u'王爺 麻豆代天府（五府）'),
            SimpleTerm(value=u'flxt33', title=u'王爺 東港東隆宮（溫府）'),
            SimpleTerm(value=u'flxt34', title=u'王爺 馬鳴山鎮安宮（五年千歲）'),
            SimpleTerm(value=u'flxt35', title=u'王爺 台西安西府（張李莫）'),
            SimpleTerm(value=u'flxt36', title=u'王爺 府城共善堂（邢府）'),
            SimpleTerm(value=u'flxt37', title=u'王爺 保西代天府'),
            SimpleTerm(value=u'flxt38', title=u'王爺 鹿港奉天宮（蘇府）'),
            SimpleTerm(value=u'flxt39', title=u'王爺 龍井福順宮（三府）'),
            SimpleTerm(value=u'flxt40', title=u'王爺 其他'),
            SimpleTerm(value=u'flxt50', title=u'觀音'),
            SimpleTerm(value=u'flxt51', title=u'觀音 萬華龍山寺'),
            SimpleTerm(value=u'flxt52', title=u'觀音 大岡山超峰寺'),
            SimpleTerm(value=u'flxt53', title=u'觀音 赤山龍湖巖'),
            SimpleTerm(value=u'flxt54', title=u'觀音 東山碧雲寺'),
            SimpleTerm(value=u'flxt55', title=u'觀音 白河大仙寺'),
            SimpleTerm(value=u'flxt56', title=u'觀音 內門紫竹寺'),
            SimpleTerm(value=u'flxt57', title=u'觀音 半天巖紫雲寺'),
            SimpleTerm(value=u'flxt58', title=u'觀音 清水紫雲巖'),
            SimpleTerm(value=u'flxt59', title=u'觀音 社頭清水巖'),
            SimpleTerm(value=u'flxt60', title=u'觀音 其他'),
            SimpleTerm(value=u'flxt81', title=u'王母（瑤池金母） 花蓮勝安宮'),
            SimpleTerm(value=u'flxt82', title=u'王母（瑤池金母） 花蓮慈惠堂'),
            SimpleTerm(value=u'flxt70', title=u'其他'),
            SimpleTerm(value=u'flxt71', title=u'其他 廣澤尊王（西羅殿）'),
            SimpleTerm(value=u'flxt72', title=u'其他 廣澤尊王（永華宮）'),
            SimpleTerm(value=u'flxt73', title=u'其他 玄天上帝（松柏嶺）'),
            SimpleTerm(value=u'flxt74', title=u'其他 玄天上帝（台南武當山）'),
            SimpleTerm(value=u'flxt75', title=u'其他 保生大帝（學甲慈濟宮）'),
            SimpleTerm(value=u'flxt76', title=u'其他 中壇元帥（新營太子宮）'),
            SimpleTerm(value=u'flxt77', title=u'其他 三山國王（荷婆崙）'),
        )
        return SimpleVocabulary(items)
flxtFactory = flxt()

class ymmy(object):
    """ YiMingMiaoYu
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'ymmy01', title=u'澎湖廟'),
            SimpleTerm(value=u'ymmy02', title=u'大陳廟'),
            SimpleTerm(value=u'ymmy03', title=u'安平廟'),
            SimpleTerm(value=u'ymmy04', title=u'東石廟'),
        )
        return SimpleVocabulary(items)
ymmyFactory = ymmy()

class xhly(object):
    """ XiangHuoLaiYuan
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'xhly01', title=u'祖先攜來'),
            SimpleTerm(value=u'xhly02', title=u'香火發光'),
            SimpleTerm(value=u'xhly03', title=u'不肯離去'),
            SimpleTerm(value=u'xhly04', title=u'撿拾神明'),
            SimpleTerm(value=u'xhly05', title=u'撿拾王船'),
            SimpleTerm(value=u'xhly06', title=u'小孩泥朔'),
            SimpleTerm(value=u'xhly07', title=u'分靈'),
            SimpleTerm(value=u'xhly08', title=u'神明指示'),
            SimpleTerm(value=u'xhly09', title=u'安鎮去疫'),
        )
        return SimpleVocabulary(items)
xhlyFactory = xhly()

class nlqs(object):
    """ NianLiQingSheng
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'nlqs01', title=u'關渡媽祖'),
            SimpleTerm(value=u'nlqs02', title=u'北港媽祖'),
            SimpleTerm(value=u'nlqs03', title=u'新港媽祖'),
            SimpleTerm(value=u'nlqs04', title=u'彰化媽祖'),
            SimpleTerm(value=u'nlqs05', title=u'五年千歲'),
        )
        return SimpleVocabulary(items)
nlqsFactory = nlqs()

class wyxx(object):
    """ WangYeXianXiang
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'wyxx01', title=u'祀船'),
            SimpleTerm(value=u'wyxx02', title=u'請王（固定）'),
            SimpleTerm(value=u'wyxx03', title=u'請王（非固定）'),
            SimpleTerm(value=u'wyxx04', title=u'送王船（固定）'),
            SimpleTerm(value=u'wyxx05', title=u'送王船（非固定）'),
            SimpleTerm(value=u'wyxx06', title=u'王醮'),
            SimpleTerm(value=u'wyxx07', title=u'其他'),
        )
        return SimpleVocabulary(items)
wyxxFactory = wyxx()

class medicine(object):
    """ Medicine Divination
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='medicine00', title=u'無'),
            SimpleTerm(value='medicine01', title=u'大人'),
            SimpleTerm(value='medicine02', title=u'小兒'),
            SimpleTerm(value='medicine03', title=u'婦科'),
            SimpleTerm(value='medicine04', title=u'眼科'),
            SimpleTerm(value='medicine05', title=u'有，其他'),
        )
        return SimpleVocabulary(items)
medicineFactory = medicine()

class luck(object):
    """ Luck Divination
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value=u'luck00', title=u'無'),
            SimpleTerm(value=u'luck01', title=u'六十首'),
            SimpleTerm(value=u'luck02', title=u'一百首'),
            SimpleTerm(value=u'luck03', title=u'有，其他'),
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

