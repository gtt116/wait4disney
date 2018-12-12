# -*-coding:utf8-*-
"""
This file contains all name mapping from English to Chinese.
"""

NAMES = {
    'MeetDroidFriends': u'与星球大战里的机器人朋友见面/星球大战远征基地/银河帝国贸易站',
    'TronLightcyclePowerRun': u'创急速光轮',
	'RoaringRapids': u'雷鸣山漂流',
	'ChallengeTrails': u'古迹探索营的绳索挑战道/古迹探索营',
	'VistaTrail': u'古迹探索营的探索步行道/古迹探索营',
	'1879': u'1879 maybe 古迹探索营/古迹探索营',
	'OnceUponTimeAdventure': u'漫游童话时光',
	'AliceWonderlandMaze': u'爱丽丝梦游仙境迷宫',
	'1882': u'1882 maybe 奇幻童话城堡',
	'HunnyPotSpin': u'旋转疯蜜罐',
	'DisneyPrincessesStorybookCourt': u'奇幻童话城堡里的迪士尼公主们',
	'PeterPansFlight': u'小飞侠天空奇遇',
	'SevenDwarfsMineTrain': u'七个小矮人矿山车',
	'AdventuresWinniePooh': u'小熊维尼历险记',
	'VoyageToCrystalGrotto': u'晶彩奇航',
	'DumboFlyingElephant': u'小飞象',
	'FantasiaCarousel': u'幻想曲旋转木马',
	'1900': u'1900 maybe 漫威英雄总部/漫威英雄总部',
	'1913': u'1913 maybe 宝藏湾的杰克船长',
	'ExplorerCanoes': u'探险家独木舟',
	'PiratesOfCaribbean': u'加勒比海盗——沉落宝藏之战',
	'ShipwreckShore': u'传奇戏水滩',
	'SirensRevenge': u'探秘海妖复仇号',
	'BuzzLightyearPlanetRescue': u'巴斯光年星际营救',
	'JetPacks': u'喷气背包飞行器',
	'StitchEncounter': u'太空幸会史迪奇',
	'1905': u'1905 is Closed',
	'SoaringOverHorizon': u'翱翔.飞跃地平线',
	'MeetMickeyGardensImagination': u'奇想花园的米奇俱乐部',
	'CaptainAmerica': u'漫威英雄总部的美国队长/漫威英雄总部',
	'JungleFriendsHappyCircle': u'欢笑聚友会的丛林迪士尼朋友们',
	'1966': u'1966 is Closed',
	'1967': u'1967',
	'1984': u'1984',
	'2281': u'2281 is See Times Guide',
	'2293': u'2293',
	'2476': u'2476 is Closed',
	'CampDiscovery': u'CampDiscovery',
	'MickeysFilmFestival': u'米奇电影节',
	'TronRealm': u'TronRealm maybe 米妮和朋友们',
	'StarWarsLaunchBay': u'星球大战远征基地/星球大战远征基地/银河帝国贸易站',
	'MarvelUniverse': u'MarvelUniverse maybe 十二朋友园',
	'2596': u'2596 is Closed',
	'SpiderMan': u'漫威英雄总部的蜘蛛侠/漫威英雄总部',
	'BecomeIronMan': u'变身钢铁侠/漫威英雄总部',
	'ScreeningRoom': u'电影放映室/星球大战远征基地/银河帝国贸易站',
	'EncounterKyloRen': u'星球大战远征基地的凯洛.伦/星球大战远征基地/银河帝国贸易站',
	'MeetDarthVader': u'星球大战远征基地的达斯.维达/星球大战远征基地/银河帝国贸易站',
	'MillenniumFalcon': u'千年隼号/星球大战远征基地/银河帝国贸易站',
    'RexsRCRacer': u'抱抱龙冲天赛车',
    'SlinkyDogSpin': u'弹簧狗团团转',
    'WoodysRoundUp': u'胡迪牛仔嘉年华'
}


def translate(en):
    return NAMES.get(en, en)
