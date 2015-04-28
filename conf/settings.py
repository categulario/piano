LEVELS = {
    "level0": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "final",
        ],
        "file": "level0.csv"
    },
    "level1": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img1",
            "final",
        ],
        "file": "level1.csv"
    },
    "level2": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img2",
            "final",
        ],
        "file": "level2.csv"
    },
    "level3": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img1",
            "img2",
            "final",
        ],
        "file": "level3.csv"
    },
    "level4": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img3",
            "final",
        ],
        "file": "level4.csv"
    },
    "level5": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img3",
            "img1",
            "final",
        ],
        "file": "level5.csv"
    },
    "level6": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img3",
            "img2",
            "final",
        ],
        "file": "level6.csv"
    },
    "level7": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img1",
            "img2",
            "img3",
            "final",
        ],
        "file": "level7.csv"
    },
    "level8": {
        "criteria": 8,
        "screens": [
            "general1",
            "general2",
            "general3",
            "img1",
            "img2",
            "img3",
            "final",
        ],
        "file": "level8.csv"
    },

    # Niveles de prueba
    "sin_cuando": {
        "criteria": 6,
        "screens": [
            "general1",
            "general2",
            "general3",
            "final",
        ],
        "file": "test.csv",
    },
}

GROUPS = {
    "aislado": [
        "level0",
        "level1",
        "level2",
        "level4",
    ],
    "progresivo": [
        "level0",
        "level1",
        "level3",
        "level8",
    ],
    "integral": [
        "level0",
        "level8",
        "level8",
        "level8",
    ],
    "prueba": [
        "sin_cuando",
    ],
}
