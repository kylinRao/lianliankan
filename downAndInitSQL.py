# coding=utf-8
from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
from lianliankan import exe

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


varall_equip = {
    "救赎之翼": {
        "rune_id": "15491",
        "name": "救赎之翼",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GQ014.jpg",
            "price": "1800",
            "detail": "",
            "parent_id": "",
            "child_id": "风之轻语,红玛瑙",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "救援",
                    "effect": "60秒CD，为周围血量最低的友方英雄(包括自己)提供一个吸收(800+英雄等级*80)伤害的护盾，并提升30%的移动速度，持续3秒!",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "极影": {
        "rune_id": "15490",
        "name": "极影",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GK501.jpg",
            "price": "1910",
            "detail": "",
            "parent_id": "",
            "child_id": "凤鸣指环,红玛瑙",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "鼓舞",
                    "effect": "60秒CD，为周围友方英雄增加50%攻击速度和20%冷却缩减，持续5秒!",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "鼓舞之盾": {
        "rune_id": "15489",
        "name": "鼓舞之盾",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GK020.jpg",
            "price": "1180",
            "detail": "",
            "parent_id": "鼓舞之盾",
            "child_id": "学识宝石,红玛瑙",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "奔腾号令",
                    "effect": "60秒CD，增加周围所有友方英雄30%移速，持续3秒",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "风灵纹章": {
        "rune_id": "15488",
        "name": "风灵纹章",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GJ522.jpg",
            "price": "1180",
            "detail": "",
            "parent_id": "奔狼纹章",
            "child_id": "学识宝石,红玛瑙",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "救援",
                    "effect": "60秒CD，增加周围所有友方英雄30%的移动速度，持续3秒",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "风之轻语": {
        "rune_id": "15487",
        "name": "风之轻语",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GJ007.jpg",
            "price": "1010",
            "detail": "",
            "parent_id": "救赎之翼",
            "child_id": "学识宝石,红玛瑙",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "救援",
                    "effect": "60秒CD，为周围血量最低的友方英雄(包括自己)提供一个吸收(500+英雄等级*50)伤害的护盾，并提升15%的移动速度，持续3秒!",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "凤鸣指环": {
        "rune_id": "15486",
        "name": "凤鸣指环",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GH953.jpg",
            "price": "1010",
            "detail": "",
            "parent_id": "极影",
            "child_id": "学识宝石,红玛瑙",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "如果自己的经济或经验是己方最低，每3秒额外获得5点经济或经验!",
                    "effect": "60秒CD，为周围友方英雄增加30%攻击速度和10%冷却缩减，持续3秒",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "学识宝石": {
        "rune_id": "15485",
        "name": "学识宝石",
        "category": "fangyu",
        "tier": "1",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170627\/70-1F62GHH5.jpg",
            "price": "300",
            "detail": "",
            "parent_id": "风鸣指环,风之轻语,风灵纹章,鼓舞之盾",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "奉献",
                    "effect": "如果自己的经济或经验是己方最低，每3秒额外获得5点经济或经验!",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "逐日之弓": {
        "rune_id": "13976",
        "name": "逐日之弓",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.18183.com\/uploads\/allimg\/170328\/36-1F32QJ230.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "狂暴双刃",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "逐日",
                    "effect": "增加自身150普攻射程和30%的移动速度，持续5秒（冷却CD60秒），仅远程英雄生效",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "噬神之书": {
        "rune_id": "11641",
        "name": "噬神之书",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.18183.duoku.com\/uploads\/allimg\/161012\/36-161012140008.png",
            "price": "1254",
            "detail": "",
            "parent_id": "",
            "child_id": "血族之书,红玛瑙,咒术典籍",
            "attribute": [
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "800",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "ability_power",
                    "value": "180",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "刻印",
                    "effect": "增加25%法术吸血",
                    "type": "unique_passive"
                }
            ],
            "suit": "露娜,高渐离,妲己,貂蝉,芈月,不知火舞"
        }
    },
    "疾步之靴": {
        "rune_id": "9798",
        "name": "疾步之靴",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/98.png",
            "price": "530",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [

            ],
            "effect": [
                {
                    "name": "神行",
                    "effect": "脱离战斗后增加60移动速度",
                    "type": "unique_passive"
                },
                {
                    "name": "",
                    "effect": "+60移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": "典韦,老夫子,钟无艳,达摩"
        }
    },
    "冰痕之握": {
        "rune_id": "9797",
        "name": "冰痕之握",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/97.png",
            "price": "2020",
            "detail": "",
            "parent_id": "",
            "child_id": "光辉之剑,布甲",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "800",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "armor",
                    "value": "200",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "咒刃",
                    "effect": "使用技能后，5秒内的下一次普攻造成范围30%减速和150点物理伤害（每升1级增加20点），这个效果有3秒冷却时间。",
                    "type": "unique_passive"
                }
            ],
            "suit": "孙尚香,赵云,橘右京"
        }
    },
    "冰霜长矛": {
        "rune_id": "9796",
        "name": "冰霜长矛",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/96.png",
            "price": "1970",
            "detail": "",
            "parent_id": "",
            "child_id": "日冕,红玛瑙,铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "80",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "600",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "碎冰",
                    "effect": "普攻会减少目标30%攻速和移速，持续2秒，远程英雄使用时减速效果持续时间衰减为1秒。",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "奔狼纹章": {
        "rune_id": "9795",
        "name": "奔狼纹章",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/95.png",
            "price": "1530",
            "detail": "",
            "parent_id": "",
            "child_id": "红玛瑙,风灵纹章",
            "attribute": [
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "armor",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "奔腾号令",
                    "effect": "60秒CD,增加周围所有友方英雄10%伤害输出和30%的移动速度,持续2秒",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "辉月": {
        "rune_id": "9794",
        "name": "辉月",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/94.png",
            "price": "2300",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒,圣者法典",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "160",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "月之守护",
                    "effect": "90秒CD,免疫所有效果,不能移动,攻击和使用技能,持续1.5秒",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "梦魇之牙": {
        "rune_id": "9793",
        "name": "梦魇之牙",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/93.png",
            "price": "2050",
            "detail": "",
            "parent_id": "大棒,元素杖",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "240",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "重伤",
                    "effect": "成伤害使得目标的生命恢复效果减少50%，持续1.5秒(如果该伤害由普攻触发，则持续时间延长至3秒)",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "金色圣剑": {
        "rune_id": "9792",
        "name": "金色圣剑",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/92.png",
            "price": "2060",
            "detail": "",
            "parent_id": "",
            "child_id": "咒术典籍,蓝宝石,圣者法典",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "ability_power",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "灼热",
                    "effect": "普通攻击造成基于自身法术强度20%的法术伤害",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "破碎圣杯": {
        "rune_id": "9791",
        "name": "破碎圣杯",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/91.png",
            "price": "900",
            "detail": "",
            "parent_id": "圣杯",
            "child_id": "咒术典籍,炼金护符",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "80",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana_regen",
                    "value": "20",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "元素杖": {
        "rune_id": "9790",
        "name": "元素杖",
        "category": "fashu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/90.png",
            "price": "540",
            "detail": "",
            "parent_id": "虚无法杖",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "80",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "制裁之刃": {
        "rune_id": "9789",
        "name": "制裁之刃",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/89.png",
            "price": "1800",
            "detail": "",
            "parent_id": "",
            "child_id": "铁剑,雷鸣刃",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "life_steal",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "重伤",
                    "effect": "造成伤害使得目标的生命恢复效果减少50%，持续1.5秒(如果该伤害由普攻触发，则持续时间延长至3秒)",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "纯净苍穹": {
        "rune_id": "9788",
        "name": "纯净苍穹",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/88.png",
            "price": "2230",
            "detail": "",
            "parent_id": "",
            "child_id": "速击之枪,冲能拳套,匕首",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "40",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "精准",
                    "effect": "普通攻击附带60点物理伤害",
                    "type": "unique_passive"
                },
                {
                    "name": "驱散",
                    "effect": "90秒CD,受到的所有伤害降低50%,持续1.5秒,可以在被控制时使用。",
                    "type": "unique_active"
                }
            ],
            "suit": ""
        }
    },
    "速击之枪": {
        "rune_id": "9787",
        "name": "速击之枪",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/87.png",
            "price": "890",
            "detail": "",
            "parent_id": "破灭君主,纯净苍穹",
            "child_id": "匕首",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "25",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "精准",
                    "effect": "普通攻击附带20-34点物理伤害（随等级提升）",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "冲能拳套": {
        "rune_id": "9786",
        "name": "冲能拳套",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/86.png",
            "price": "550",
            "detail": "",
            "parent_id": "",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "critical_strike_chance",
                    "value": "15",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "雷鸣刃": {
        "rune_id": "9785",
        "name": "雷鸣刃",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/85.png",
            "price": "450",
            "detail": "",
            "parent_id": "破魔刀,名刀·司命,破甲弓,制裁之刃",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "40",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "血魔之怒": {
        "rune_id": "9783",
        "name": "血魔之怒",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/83.png",
            "price": "2120",
            "detail": "",
            "parent_id": "",
            "child_id": "力量腰带,铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "20",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1000",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "血怒",
                    "effect": "生命值低于30%时获得血怒，增加80点攻击与强大护盾持续8秒，效果有90秒CD",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "回响之杖": {
        "rune_id": "9782",
        "name": "回响之杖",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/82.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "240",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "7",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "回响",
                    "effect": "技能命中会触发小范围爆炸造成50（+50%法术加成）法术伤害，这个效果有5秒CD",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "暴烈之甲": {
        "rune_id": "9781",
        "name": "暴烈之甲",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/81.png",
            "price": "1820",
            "detail": "",
            "parent_id": "",
            "child_id": "力量腰带,布甲",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "60",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1000",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "无畏",
                    "effect": "受到伤害获得1层增益，每层提供2%移速和2%伤害输出率，最高5层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "贤者的庇护": {
        "rune_id": "9780",
        "name": "贤者的庇护",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/80.png",
            "price": "2080",
            "detail": "",
            "parent_id": "",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "140",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "magic_resist",
                    "value": "140",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "复生",
                    "effect": "复活时拥有2000+英雄等级*100点生命值，这个效果有3分钟CD",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "极寒风暴": {
        "rune_id": "9779",
        "name": "极寒风暴",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.18183.com\/uploads\/allimg\/170328\/36-1F32QK455.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "雪山圆盾,守护者之铠",
            "attribute": [
                {
                    "attribute": "cooldown_reduction",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "armor",
                    "value": "360",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "寒冰冲击",
                    "effect": "受到单次伤害超过当前生命值10%时触发寒冰冲击，对周围敌人造成伤害并降低其30%攻击和移动速度，持续2秒，这个效果有2秒内置CD",
                    "type": "unique_passive"
                }
            ],
            "suit": "刘邦,貂蝉"
        }
    },
    "魔女斗篷": {
        "rune_id": "9778",
        "name": "魔女斗篷",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/78.png",
            "price": "1870",
            "detail": "",
            "parent_id": "",
            "child_id": "神隐斗篷,力量腰带",
            "attribute": [
                {
                    "attribute": "magic_resist",
                    "value": "360",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1000",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "迷雾",
                    "effect": "脱离战斗3秒后刷新,获得一个吸收320~2000点法术伤害的护盾（护盾效果随英雄等级成长）",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "不死鸟之眼": {
        "rune_id": "9777",
        "name": "不死鸟之眼",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.18183.com\/uploads\/allimg\/170328\/36-1F32QK246.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "神隐斗篷,红玛瑙,提神水晶",
            "attribute": [
                {
                    "attribute": "magic_resist",
                    "value": "240",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1200",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health_regen",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "血统",
                    "effect": "受到的治疗效果提升10%，血量低于50%时，治疗效果加成会增加到30%",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "不祥征兆": {
        "rune_id": "9776",
        "name": "不祥征兆",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/76.png",
            "price": "2180",
            "detail": "",
            "parent_id": "",
            "child_id": "力量腰带,守护者之铠",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "270",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1200",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "寒铁",
                    "effect": "受到攻击会减少攻击者30%攻击速度与15%移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "霸者重装": {
        "rune_id": "9775",
        "name": "霸者重装",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/75.png",
            "price": "2370",
            "detail": "",
            "parent_id": "",
            "child_id": "力量腰带",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "2000",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health_regen",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "复苏",
                    "effect": "脱离战斗后每秒恢复2%最大生命值",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "红莲斗篷": {
        "rune_id": "9774",
        "name": "红莲斗篷",
        "category": "fangyu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/74.png",
            "price": "1830",
            "detail": "",
            "parent_id": "",
            "child_id": "熔炼之心,布甲",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "240",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1200",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "献祭",
                    "effect": "每秒对身边的敌军造成100点法术伤害",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "反伤刺甲": {
        "rune_id": "9772",
        "name": "反伤刺甲",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/72.png",
            "price": "1840",
            "detail": "",
            "parent_id": "",
            "child_id": "布甲,雷鸣刃",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "420",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "attack_damage",
                    "value": "40",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "荆棘",
                    "effect": "受到物理伤害时，会将伤害量的15%以法术伤害的形式回敬给对方（按照计算伤害减免之前的初始伤害值计算）",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "近卫荣耀": {
        "rune_id": "9771",
        "name": "近卫荣耀",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170206\/70-1F2061T002.png",
            "price": "1510",
            "detail": "",
            "parent_id": "",
            "child_id": "红玛瑙,鼓舞之盾",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "军团",
                    "effect": "周围友军增加(30+英雄等级*2)点物理攻击和(60+英雄等级*4)点法术攻击",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "守护者之铠": {
        "rune_id": "9770",
        "name": "守护者之铠",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/70.png",
            "price": "730",
            "detail": "",
            "parent_id": "不祥征兆,冰封之心",
            "child_id": "布甲",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "210",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "寒铁",
                    "effect": "受到攻击会减少攻击者15%攻击速度,持续3秒",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "雪山圆盾": {
        "rune_id": "9769",
        "name": "雪山圆盾",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/69.png",
            "price": "900",
            "detail": "",
            "parent_id": "冰封之心,冰脉护手",
            "child_id": "布甲",
            "attribute": [
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "armor",
                    "value": "110",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "神隐斗篷": {
        "rune_id": "9768",
        "name": "神隐斗篷",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/68.png",
            "price": "1020",
            "detail": "",
            "parent_id": "振兴之铠,魔女斗篷",
            "child_id": "红玛瑙,抗魔披风",
            "attribute": [
                {
                    "attribute": "magic_resist",
                    "value": "120",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "700",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health_regen",
                    "value": "50",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "suit": ""
        }
    },
    "熔炼之心": {
        "rune_id": "9767",
        "name": "熔炼之心",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/67.png",
            "price": "900",
            "detail": "",
            "parent_id": "红莲斗篷",
            "child_id": "红玛瑙",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "700",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "献祭",
                    "effect": "每秒对身边的敌军造成60点法术伤害,每升1级增加2点伤害",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "力量腰带": {
        "rune_id": "9766",
        "name": "力量腰带",
        "category": "fangyu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/66.png",
            "price": "900",
            "detail": "",
            "parent_id": "霸者重装,不祥征兆,暴烈之甲,冰霜法杖,魔女斗篷",
            "child_id": "红玛瑙",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "1000",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "提神水晶": {
        "rune_id": "9765",
        "name": "提神水晶",
        "category": "fangyu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/65.png",
            "price": "140",
            "detail": "",
            "parent_id": "霸者重装,振兴之铠",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "health_regen",
                    "value": "30",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "抗魔披风": {
        "rune_id": "9764",
        "name": "抗魔披风",
        "category": "fangyu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/64.png",
            "price": "220",
            "detail": "",
            "parent_id": "神隐斗篷,军团荣耀,抵抗之靴,梦魇之牙",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "magic_resist",
                    "value": "90",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "布甲": {
        "rune_id": "9763",
        "name": "布甲",
        "category": "fangyu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/63.png",
            "price": "220",
            "detail": "",
            "parent_id": "雪山圆盾,守护者之铠,军团荣耀,反伤刺甲,奔狼纹章,爆烈之甲,影忍之足,红莲斗篷",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "90",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "红玛瑙": {
        "rune_id": "9762",
        "name": "红玛瑙",
        "category": "fangyu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/62.png",
            "price": "300",
            "detail": "",
            "parent_id": "力量腰带,熔炼之心,神隐斗篷,近卫荣耀,血魔之怒,奔狼纹章,噬神之书,",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "300",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "贪婪之噬": {
        "rune_id": "9761",
        "name": "贪婪之噬",
        "category": "daye",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/61.png",
            "price": "1460",
            "detail": "",
            "parent_id": "",
            "child_id": "追击刀锋",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "45",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "attack_speed",
                    "value": "12",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身2%攻击速度，最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "巨人之握": {
        "rune_id": "9760",
        "name": "巨人之握",
        "category": "daye",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/60.png",
            "price": "1500",
            "detail": "",
            "parent_id": "",
            "child_id": "巡守利斧",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "600",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "献祭",
                    "effect": "每秒对附近敌人造成60点法术伤害",
                    "type": "unique_passive"
                },
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身70点最大生命，最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "符文大剑": {
        "rune_id": "9759",
        "name": "符文大剑",
        "category": "daye",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/59.png",
            "price": "1490",
            "detail": "",
            "parent_id": "",
            "child_id": "游击宽刃",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "咒刃",
                    "effect": "使用技能强化下一次普攻",
                    "type": "unique_passive"
                },
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身8点法术强度，最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "追击刀锋": {
        "rune_id": "9758",
        "name": "追击刀锋",
        "category": "daye",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/58.png",
            "price": "750",
            "detail": "",
            "parent_id": "贪婪之噬",
            "child_id": "狩猎宽刃",
            "attribute": [

            ],
            "effect": [
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身2%攻击速度,最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "巡守利斧": {
        "rune_id": "9757",
        "name": "巡守利斧",
        "category": "daye",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/57.png",
            "price": "750",
            "detail": "",
            "parent_id": "巨人之握",
            "child_id": "狩猎宽刃",
            "effect": [
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身70点最大生命,最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "游击宽刃": {
        "rune_id": "9756",
        "name": "游击宽刃",
        "category": "daye",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/56.png",
            "price": "750",
            "detail": "",
            "parent_id": "符文大剑",
            "child_id": "狩猎宽刃",
            "attribute": [

            ],
            "effect": [
                {
                    "name": "打野",
                    "effect": "增加30%对野怪的伤害，击杀野怪获得经验提升30%",
                    "type": "unique_passive"
                },
                {
                    "name": "磨砺",
                    "effect": "击杀野怪增加自身8点法术强度,最多叠加15层",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "急速战靴": {
        "rune_id": "9755",
        "name": "急速战靴",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/55.png",
            "price": "710",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "30",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+60移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "秘法之靴": {
        "rune_id": "9754",
        "name": "秘法之靴",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/54.png",
            "price": "710",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [
                {
                    "attribute": "movement_speed",
                    "value": "60",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+75法术穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "冷静之靴": {
        "rune_id": "9753",
        "name": "冷静之靴",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/53.png",
            "price": "710",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [
                {
                    "attribute": "cooldown_reduction",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+60移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "抵抗之靴": {
        "rune_id": "9752",
        "name": "抵抗之靴",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/52.png",
            "price": "710",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [
                {
                    "attribute": "magic_resist",
                    "value": "110",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+60移动速度",
                    "type": "unique_passive"
                },
                {
                    "name": "",
                    "effect": "+35%韧性",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "影忍之足": {
        "rune_id": "9751",
        "name": "影忍之足",
        "category": "yidong",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/51.png",
            "price": "710",
            "detail": "",
            "parent_id": "",
            "child_id": "神速之靴",
            "attribute": [
                {
                    "attribute": "armor",
                    "value": "110",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+60移动速度",
                    "type": "unique_passive"
                },
                {
                    "name": "",
                    "effect": "减少15%受到普通攻击的伤害",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "神速之靴": {
        "rune_id": "9750",
        "name": "神速之靴",
        "category": "yidong",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/50.png",
            "price": "250",
            "detail": "",
            "parent_id": "影忍之足,抵抗之靴,冷静之靴,秘法之靴,急速战靴,疾步之靴",
            "child_id": "",
            "attribute": [

            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+30移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "狩猎宽刃": {
        "rune_id": "9749",
        "name": "狩猎宽刃",
        "category": "daye",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/49.png",
            "price": "250",
            "detail": "",
            "parent_id": "游击宽刃,巡守利斧,追击刀锋",
            "child_id": "",
            "attribute": [

            ],
            "effect": [
                {
                    "name": "打野",
                    "effect": "增加20%对野怪的伤害，击杀野怪获得经验提升20%",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "贤者之书": {
        "rune_id": "9748",
        "name": "贤者之书",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/48.png",
            "price": "2990",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "刻印",
                    "effect": "增加1400点生命",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "时之预言": {
        "rune_id": "9747",
        "name": "时之预言",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/47.png",
            "price": "2090",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒,进化水晶",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "160",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "600",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "800",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "守护",
                    "effect": "每5点法强提升1点物理和法术防御，最多提升200点。",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "巫术法杖": {
        "rune_id": "9746",
        "name": "巫术法杖",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/46.png",
            "price": "2120",
            "detail": "",
            "parent_id": "",
            "child_id": "光辉之剑,咒术典籍",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "140",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "8",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "咒刃",
                    "effect": "使用技能后，下一次普通攻击附加高额法术伤害，这个效果有2秒的冷却时间",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "痛苦面具": {
        "rune_id": "9745",
        "name": "痛苦面具",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/45.png",
            "price": "2040",
            "detail": "",
            "parent_id": "",
            "child_id": "魅影面罩,咒术典籍",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "140",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "折磨",
                    "effect": "3秒持续灼烧，每秒造成相当于目标当前生命值3%的法术伤害",
                    "type": "unique_passive"
                },
                {
                    "name": "",
                    "effect": "+75法术穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "冰霜法杖": {
        "rune_id": "9744",
        "name": "冰霜法杖",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/44.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒,力量腰带",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "150",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "1050",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "结霜",
                    "effect": "英雄技能造成伤害会附带20%的减速效果,持续2秒",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "博学者之怒": {
        "rune_id": "9743",
        "name": "博学者之怒",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/43.png",
            "price": "2300",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒,咒术典籍",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "240",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "毁灭",
                    "effect": "法术强度提升35%",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "虚无法杖": {
        "rune_id": "9742",
        "name": "虚无法杖",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/42.png",
            "price": "1520",
            "detail": "",
            "parent_id": "",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "180",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "45%法术穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "炽热支配者": {
        "rune_id": "9741",
        "name": "炽热支配者",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/41.png",
            "price": "1950",
            "detail": "",
            "parent_id": "",
            "child_id": "大棒,蓝宝石,炼金护符",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "180",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "600",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana_regen",
                    "value": "15",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "法力护盾",
                    "effect": "生命值低于30%时，获得一个吸收伤害的护盾，吸收伤害受等级成长及法术加成，被动效果触发时额外增加30%移动速度",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "圣杯": {
        "rune_id": "9740",
        "name": "圣杯",
        "category": "fashu",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/40.png",
            "price": "2030",
            "detail": "",
            "parent_id": "",
            "child_id": "咒术典籍,炼金护符,圣者法典,破碎圣杯",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "180",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana_regen",
                    "value": "25",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "法力源泉",
                    "effect": "每5秒恢复5%最大法力值",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "进化水晶": {
        "rune_id": "9739",
        "name": "进化水晶",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/39.png",
            "price": "720",
            "detail": "",
            "parent_id": "时之预言",
            "child_id": "蓝宝石,红玛瑙",
            "attribute": [
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "英勇奖赏",
                    "effect": "升级后在3秒内回复20%生命值与法力值",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "魅影面罩": {
        "rune_id": "9738",
        "name": "魅影面罩",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/38.png",
            "price": "1020",
            "detail": "",
            "parent_id": "痛苦面具,虚无法杖",
            "child_id": "咒术典籍,红玛瑙",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "70",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "300",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "75法术穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "光辉之剑": {
        "rune_id": "9737",
        "name": "光辉之剑",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/37.png",
            "price": "780",
            "detail": "",
            "parent_id": "巫术法杖,冰痕之握",
            "child_id": "红玛瑙,蓝宝石",
            "attribute": [
                {
                    "attribute": "health",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "咒刃",
                    "effect": "使用技能后，下一次普通攻击附加法术伤害，这个效果有2秒的冷却时间",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "血族之书": {
        "rune_id": "9736",
        "name": "血族之书",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/36.png",
            "price": "1240",
            "detail": "",
            "parent_id": "",
            "child_id": "咒术典籍,圣者法典",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "75",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "增加20%法术吸血",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "大棒": {
        "rune_id": "9735",
        "name": "大棒",
        "category": "fashu",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/35.png",
            "price": "820",
            "detail": "",
            "parent_id": "博学者之怒,冰霜法杖,时之预言,贤者之书,回响之杖,辉月,梦魇之牙",
            "child_id": "咒术典籍",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "120",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "圣者法典": {
        "rune_id": "9734",
        "name": "圣者法典",
        "category": "fashu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/34.png",
            "price": "500",
            "detail": "",
            "parent_id": "血族之书,圣杯,辉月",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "20",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "8",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "炼金护符": {
        "rune_id": "9733",
        "name": "炼金护符",
        "category": "fashu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/33.png",
            "price": "120",
            "detail": "",
            "parent_id": "炽热支配者,破碎圣杯",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "mana_regen",
                    "value": "10",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "蓝宝石": {
        "rune_id": "9732",
        "name": "蓝宝石",
        "category": "fashu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/32.png",
            "price": "220",
            "detail": "",
            "parent_id": "光辉之剑,进化水晶,炽热支配者,雪山圆盾,符文大剑",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "mana",
                    "value": "300",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "咒术典籍": {
        "rune_id": "9731",
        "name": "咒术典籍",
        "category": "fashu",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/31.png",
            "price": "300",
            "detail": "",
            "parent_id": "大棒,血族之书,光辉之剑,魅影面罩,圣杯,炽热支配者,破碎圣杯,噬神之书",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "ability_power",
                    "value": "40",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "破军": {
        "rune_id": "9730",
        "name": "破军",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/30.png",
            "price": "2950",
            "detail": "",
            "parent_id": "",
            "child_id": "风暴巨剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "200",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "破军",
                    "effect": "目标生命低于50%时伤害提高30%",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "暗影战斧": {
        "rune_id": "9729",
        "name": "暗影战斧",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/29.png",
            "price": "2090",
            "detail": "",
            "parent_id": "",
            "child_id": "日冕,陨星",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "85",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "500",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "残废",
                    "effect": "普通攻击有30%几率降低敌人20%移动速度，持续2秒。",
                    "type": "unique_passive"
                },
                {
                    "name": "切割",
                    "effect": "增加(100+英雄等级*10)点护甲穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "影刃": {
        "rune_id": "9728",
        "name": "影刃",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/28.png",
            "price": "2070",
            "detail": "",
            "parent_id": "",
            "child_id": "狂暴双刃,匕首",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "40",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "暴风",
                    "effect": "暴击后提升自身20%攻击速度，持续2秒",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "闪电匕首": {
        "rune_id": "9727",
        "name": "闪电匕首",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/27.png",
            "price": "1840",
            "detail": "",
            "parent_id": "",
            "child_id": "狂暴双刃,搏击拳套",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "30",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "8",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "电弧",
                    "effect": "普通攻击有30%几率释放连锁闪电，对目标造成100法术伤害（该效果有0.5秒CD）",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "宗师之力": {
        "rune_id": "9726",
        "name": "宗师之力",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170206\/70-1F2061SP7.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "日冕,狂暴双刃,光辉之剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "60",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "mana",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "400",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "咒刃",
                    "effect": "下次攻击造成额外100%物理加成的伤害",
                    "type": "unique_passive"
                },
                {
                    "name": "残废",
                    "effect": "普通攻击有30%几率降低敌人20%移动速度，持续2秒",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "无尽战刃": {
        "rune_id": "9725",
        "name": "无尽战刃",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/25.png",
            "price": "2140",
            "detail": "",
            "parent_id": "",
            "child_id": "风暴巨剑,冲能拳套,铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "120",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "20",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+50%暴击效果",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "泣血之刃": {
        "rune_id": "9724",
        "name": "泣血之刃",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/24.png",
            "price": "1740",
            "detail": "",
            "parent_id": "",
            "child_id": "风暴巨剑,吸血之镰",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "life_steal",
                    "value": "25",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "破甲弓": {
        "rune_id": "9723",
        "name": "破甲弓",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/23.png",
            "price": "2100",
            "detail": "",
            "parent_id": "",
            "child_id": "铁剑,陨星",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "80",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+45%物理护甲穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "名刀·司命": {
        "rune_id": "9722",
        "name": "名刀·司命",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/22.png",
            "price": "1760",
            "detail": "",
            "parent_id": "",
            "child_id": "铁剑,雷鸣刃",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "60",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "暗幕",
                    "effect": "免疫致命伤并免疫伤害、增加20%移动速度持续1秒近战\/0.5秒远程，90秒冷却",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "末世": {
        "rune_id": "9721",
        "name": "末世",
        "category": "gongji",
        "tier": "3",
        "info": {
            "icon": "http:\/\/img.18183.com\/uploads\/allimg\/170328\/36-1F32QK114.png",
            "price": "2160",
            "detail": "",
            "parent_id": "",
            "child_id": "吸血之镰,雷鸣刃,匕首,速击之枪",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "60",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "attack_speed",
                    "value": "30",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "life_steal",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "破败",
                    "effect": "普通攻击附带目标当前生命值8%的物理伤害（对野怪最多：80）",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "破魔刀": {
        "rune_id": "9720",
        "name": "破魔刀",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/20.png",
            "price": "2000",
            "detail": "",
            "parent_id": "",
            "child_id": "风暴巨剑,抗魔披风",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "100",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "magic_resist",
                    "value": "50",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "破魔",
                    "effect": "增加等同于自身物理攻击40%的法术防御，最多增加300点",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "陨星": {
        "rune_id": "9719",
        "name": "陨星",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170609\/70-1F609101559.png",
            "price": "1080",
            "detail": "",
            "parent_id": "暗影战斧,破甲弓",
            "child_id": "铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "45",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "cooldown_reduction",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "",
                    "effect": "+60护甲穿透",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "狂暴双刃": {
        "rune_id": "9718",
        "name": "狂暴双刃",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/18.png",
            "price": "890",
            "detail": "",
            "parent_id": "三圣之力,闪电匕首,影刃",
            "child_id": "匕首,搏击拳套",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "15",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "critical_strike_chance",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "movement_speed",
                    "value": "5",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "搏击拳套": {
        "rune_id": "9717",
        "name": "搏击拳套",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/17.png",
            "price": "320",
            "detail": "",
            "parent_id": "狂暴双刃,闪电匕首",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "critical_strike_chance",
                    "value": "8",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "匕首": {
        "rune_id": "9716",
        "name": "匕首",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/16.png",
            "price": "290",
            "detail": "",
            "parent_id": "狂暴双刃,破灭君主,速击之枪,影刃,纯净苍穹",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "attack_speed",
                    "value": "10",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "铁剑": {
        "rune_id": "9715",
        "name": "铁剑",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/15.png",
            "price": "250",
            "detail": "",
            "parent_id": "风暴巨剑,日冕,凶残之力,破魔刀,破灭君主,名刀·司命,破甲弓,制裁之刃",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "20",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "日冕": {
        "rune_id": "9714",
        "name": "日冕",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "\/\/img.18183.com\/uploads\/allimg\/170206\/70-1F2061SA9.png",
            "price": "790",
            "detail": "",
            "parent_id": "宗师之力,暗影战斧",
            "child_id": "铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "40",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                },
                {
                    "attribute": "health",
                    "value": "300",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [
                {
                    "name": "残废",
                    "effect": "普通攻击有30%几率降低敌人20%移动速度，持续2秒。",
                    "type": "unique_passive"
                }
            ],
            "suit": ""
        }
    },
    "风暴巨剑": {
        "rune_id": "9713",
        "name": "风暴巨剑",
        "category": "gongji",
        "tier": "2",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/13.png",
            "price": "910",
            "detail": "",
            "parent_id": "泣血之刃,无尽战刃,破军,冰霜长矛,反伤刺甲",
            "child_id": "铁剑",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "80",
                    "unit": "point",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    },
    "吸血之镰": {
        "rune_id": "9712",
        "name": "吸血之镰",
        "category": "gongji",
        "tier": "1",
        "info": {
            "icon": "http:\/\/img.bugu.18183.com\/db_18183\/static\/wzry\/static\/images\/equips\/12.png",
            "price": "410",
            "detail": "",
            "parent_id": "破灭君主,泣血之刃",
            "child_id": "",
            "attribute": [
                {
                    "attribute": "attack_damage",
                    "value": "10",
                    "unit": "point",
                    "type": "effect",
                    "unique": "0"
                },
                {
                    "attribute": "life_steal",
                    "value": "8",
                    "unit": "percent",
                    "type": "normal",
                    "unique": "0"
                }
            ],
            "effect": [

            ],
            "suit": ""
        }
    }
}

count = 0
for k,v in varall_equip.items():
    count = count + 1
    print "total {len},now in {count}".format(len=varall_equip.__len__(),count=count)
    detailUrl = "http://db.18183.com/wzry/equip/{rune_id}.html".format(rune_id=v['rune_id'])
    response = urllib.urlopen(detailUrl).read()
    soup = BeautifulSoup(response)
    detailfFullSoup = soup.find("div",attrs={'class':'mod-bg fl'})

    detailBaseSoup = soup.find("div",attrs={'class':'equip-base-info'})
    basicSkillSoup = soup.findAll("div",attrs={'class':'equip-panel-info'})[0]
    junSkillSoup =soup.findAll("div",attrs={'class':'equip-panel-info'})[1]

    name = v['name']
    smallPic = v['info']['icon'].replace('\\','')
    if smallPic.startswith('//'):
        smallPic = "http:"+smallPic
    bigPic =detailBaseSoup.find('img').get("src").replace('\\','')
    if bigPic.startswith('//'):
        bigPic = "http:"+bigPic
    price = v['info']['price']
    basicPro =  ''
    for ali in basicSkillSoup.findAll("li"):
        basicPro = basicPro + ali.contents[0].contents[0] +ali.contents[1]
    skill = ''
    for ali in junSkillSoup.findAll("li"):
        skill = skill + ali.contents[0].contents[0] +ali.contents[1]



    if exe('select aid from Store where name = "{name}"'.format(name=name)):
        pass
    else:
        sql = 'insert into Store (pic,name,price,basicPro,skill) values ("{pic}","{name}",{price},"{basicPro}","{skill}");'.format(
                name=name,pic=smallPic,price=price,basicPro=basicPro,skill=skill)
        exe(sql)
