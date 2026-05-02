"""
Goldpatent Bot - Davlat bojlari tariflar bazasi
2026 yil ma'lumotlari
"""

# 1 BHM (Bazaviy Hisoblash Miqdori)
BHM = 412000  # so'm

TARIFFS = {
    "application": {
        # Talabnoma topshirish (mohiyat ekspertizasi shu yerga kiradi)
        "ordinary": {
            "individual": {"base": 1648000, "additional": 206000},
            "legal":      {"base": 2472000, "additional": 412000}
        },
        "collective": {
            "individual": {"base": 1648000, "additional": 206000},
            "legal":      {"base": 2472000, "additional": 412000}
        }
    },
    "express": {
        # Tezkor ekspertiza
        "base": 5600000,
        "additional": 470000
    },
    "certificate": {
        # Guvohnoma berish va 10 yillik huquq
        "ordinary": {
            "individual": {"base": 2801600, "additional": 412000},
            "legal":      {"base": 4779200, "additional": 1648000}
        },
        "collective": {
            "individual": {"base": 2801600, "additional": 412000},
            "legal":      {"base": 4779200, "additional": 1648000}
        }
    },
    "extension": {
        # Muddatni uzaytirish (10 yilga)
        "ordinary": {
            "individual": {"base": 1648000, "additional": 412000},
            "legal":      {"base": 2472000, "additional": 1648000}
        },
        "collective": {
            "individual": {"base": 2472000, "additional": 412000},
            "legal":      {"base": 4944000, "additional": 824000}
        }
    }
}


def calculate_stage(stage: str, applicant: str, mark_type: str, classes: int) -> dict:
    """
    Bitta bosqich uchun hisob-kitob qiladi.
    
    Args:
        stage: 'application', 'express', 'certificate', 'extension'
        applicant: 'individual' yoki 'legal'
        mark_type: 'ordinary' yoki 'collective'
        classes: 1 dan 45 gacha
    
    Returns:
        {'total': int, 'base': int, 'additional': int, 'formula': str}
    """
    if stage == 'express':
        base = TARIFFS['express']['base']
        additional = TARIFFS['express']['additional']
        total = base + (classes - 1) * additional
        formula = (f"{format_money(base)} (1 sinf)" if classes == 1 
                   else f"{format_money(base)} + {classes - 1} × {format_money(additional)}")
        return {
            'total': total,
            'base': base,
            'additional': additional,
            'formula': formula
        }
    
    tariff = TARIFFS[stage][mark_type][applicant]
    total = tariff['base'] + (classes - 1) * tariff['additional']
    formula = (f"{format_money(tariff['base'])} (1 sinf)" if classes == 1 
               else f"{format_money(tariff['base'])} + {classes - 1} × {format_money(tariff['additional'])}")
    
    return {
        'total': total,
        'base': tariff['base'],
        'additional': tariff['additional'],
        'formula': formula
    }


def calculate_total(stages: list, applicant: str, mark_type: str, classes: int) -> dict:
    """
    Bir nechta bosqich uchun umumiy hisob-kitob.
    
    Returns:
        {'total': int, 'breakdown': [{'stage': str, 'amount': int, 'formula': str}, ...]}
    """
    breakdown = []
    total = 0
    
    for stage in stages:
        result = calculate_stage(stage, applicant, mark_type, classes)
        breakdown.append({
            'stage': stage,
            'amount': result['total'],
            'formula': result['formula']
        })
        total += result['total']
    
    return {
        'total': total,
        'breakdown': breakdown
    }


def format_money(amount: int) -> str:
    """1234567 -> '1 234 567'"""
    return f"{amount:,}".replace(',', ' ')
