Config.CocinaTier3 = {
-------------------------------------------------
-- NIVEL 0
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Carne con menta",
    Desc = "1x Carne de ganadera, 1x Menta, 1x Limón",
    Reward = {{
        name = "carne_calidad_menta",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_calidad",
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Ancas de rana con menta",
    Desc = "1x Ancas de rana, 1x Menta, 1x Mantequilla, 1x Sartén (↺)",
    Reward = {{
        name = "ancas_rana_menta",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "ancas_rana",
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }, {
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pan de maíz (2)",
    Desc = "1x Agua, 1x Maíz, 1x Sartén (↺)",
    Reward = {{
        name = "pan_maiz",
        count = 2
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "water",
        count = 1,
        take = true
    }, {
        name = "corn",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Carne de ave con tomillo",
    Desc = "1x Carne de ave, 1x Tomillo, 1x Manteca, 1x Sartén (↺)",
    Reward = {{
        name = "carne_ave_tomillo",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "carne_ave",
        count = 1,
        take = true
    }, {
        name = "manteca",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Gachas",
    Desc = "1x Harina, 2x Ajo, 1x Agua, 1x Olla (↺)",
    Reward = {{
        name = "gachas",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 2,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},

-------------------------------------------------
-- NIVEL 1
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pescado relleno",
    Desc = "1x Pescado, 4x Patata, 1x Pepino, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pescado_relleno",
        count = 1
    }, {
        name = "fishoil",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "patata",
        count = 4,
        take = true
    }, {
        name = "pepino",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Patata horneada",
    Desc = "2x Patata, 2x Tomillo",
    Reward = {{
        name = "patata_horno",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "patata",
        count = 2,
        take = true
    }, {
        name = "thyme",
        count = 2,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Albóndigas con tómate",
    Desc = "1x Huevo de pato, 1x Pan, 1x Leche, 1x Harina, 1x Carne de ave, 1x Olla (↺)",
    Reward = {{
        name = "albondigas",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "huevo_pato",
        count = 1,
        take = true
    }, {
        name = "bread",
        count = 1,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "carne_ave",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Aros de cebolla (3)",
    Desc = "1x Cebolla, 1x Harina de maiz, 1x Vaso de cerveza rubia, 1x Sartén (↺)",
    Reward = {{
        name = "aros_cebolla",
        count = 3
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina_maiz",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "vaso_cerveza_rubia",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 2
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Bollo de canela (2)",
    Desc = "1x Harina de maíz, 2x Canela, 1x Leche, 1x Huevo, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "bollo_canela",
        count = 2
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina_maiz",
        count = 1,
        take = true
    }, {
        name = "canela",
        count = 2,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Carne de calidad con orégano",
    Desc = "1x Carne ganadera, 1x Orégano, 1x Manteca, 1x Sartén (↺)",
    Reward = {{
        name = "carne_calidad_oregano",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_calidad",
        count = 1,
        take = true
    }, {
        name = "herb_oregano",
        count = 2,
        take = true
    }, {
        name = "manteca",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Emparedado de salchicha",
    Desc = "1x Salchicha, 1x Cuña de queso, 2x Pan de maiz",
    Reward = {{
        name = "emparedado_salchicha",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "salchicha",
        count = 1,
        take = true
    }, {
        name = "consumable_cheese_wedge",
        count = 1,
        take = true
    }, {
        name = "pan_maiz",
        count = 2,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pastel de fresa",
    Desc = "1x Mantequilla, 1x Azúcar, 1x Harina, 2x Huevo, 3x Fresa, 1x Leche, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pastel_fresa",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "strawberrie",
        count = 3,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 3
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Patatata rellena",
    Desc = "1x Patata, 1x Carne, 1x Orégano, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "patata_rellena",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "patata",
        count = 1,
        take = true
    }, {
        name = "carne",
        count = 1,
        take = true
    }, {
        name = "herb_oregano",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Alubias Guisadas",
    Desc = "1x Alubias, 1x Morcilla, 1x Agua, 1x Zanahoria, 1x Ajo, 1x Patata, 1x Cebolla, 1x Olla (↺)",
    Reward = {{
        name = "alubias_guisadas",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "alubias",
        count = 1,
        take = true
    }, {
        name = "morcilla",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "consumable_carrot",
        count = 1,
        take = false
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "patata",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Cebolla rellena",
    Desc = "1x Cebolla, 1x Carne, 1x Zanahoria, 1x Patata, 1x Guisantes, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "cebolla_rellena",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "carne",
        count = 1,
        take = true
    }, {
        name = "consumable_carrot",
        count = 1,
        take = true
    }, {
        name = "patata",
        count = 1,
        take = true
    }, {
        name = "guisantes",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Hornada de galletas (8)",
    Desc = "1x Harina, 2x Huevo, 3x Cacahuetes, 1x Mantequilla, 1x Canela, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "galletas",
        count = 8
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "cacahuetes",
        count = 3,
        take = true
    }, {
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "canela",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pastel de morcilla",
    Desc = "1x Morcilla, 1x Huevo, 1x Pan, 1x Cebolla, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pastel_morcilla",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "morcilla",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "bread",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 4
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Alubias , salchicha y huevo",
    Desc = "1x Alubias, 1x Salchicha, 1x Huevo de ganso, 1x Sartén (↺)",
    Reward = {{
        name = "alubias_huevo",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "alubias",
        count = 1,
        take = true
    }, {
        name = "salchicha",
        count = 1,
        take = true
    }, {
        name = "huevo_ganso",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Cacao con leche y canela",
    Desc = "2x Cacao, 1x Leche, 1x Canela, 1 x Taza",
    Reward = {{
        name = "cacao_canela",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cacao",
        count = 2,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "canela",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Emparedado de cecina",
    Desc = "1x Cecina, 1x Queso de cabra, 2x Pan",
    Reward = {{
        name = "emparedado_cecina",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cecina",
        count = 1,
        take = true
    }, {
        name = "consumable_cabra",
        count = 1,
        take = true
    }, {
        name = "bread",
        count = 2,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Guiso casero",
    Desc = "2x Zanahoria, 2x Agua, 2x Carne de ave, 1x Tomillo, 1x Pepino, 1x Olla (↺)",
    Reward = {{
        name = "guiso_casero",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_carrot",
        count = 2,
        take = true
    }, {
        name = "water",
        count = 2,
        take = true
    }, {
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "pepino",
        count = 1,
        take = true
    }, {
        name = "carne_ave",
        count = 2,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pastel de arándano",
    Desc = "1x Mantequilla, 1x Azúcar, 1x Harina, 2x Huevo, 3x Arándano, 1x Leche, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pastel_blueberry",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "blueberry",
        count = 3,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 5
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Empanada de carne",
    Desc = "1x Harina, 1x Carne de ganadera, 1x Huevo, 1x Cebolla, 1x Tomate, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "empanada_carne",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "carne_calidad",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Chocolate a la taza",
    Desc = "1x Chocolate negro, 1x Leche, 1x Taza",
    Reward = {{
        name = "chocolate_taza",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_chocolate_negro",
        count = 1,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Guiso de pescado",
    Desc = "1x Harina de maíz, 1x Cebolla, 1x Tomate, 1x Patata, 1x Pescado, 1x Olla (↺)",
    Reward = {{
        name = "guiso_pescado",
        count = 1
    }, {
        name = "fishoil",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina_maiz",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 1,
        take = true
    }, {
        name = "patata",
        count = 1,
        take = true
    }, {
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pescado al horno",
    Desc = "1x Pescado, 2x Patata, 1x Orégano, 1x Vaso de vinagre, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pescado_horno",
        count = 1
    }, {
        name = "fishoil",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "patata",
        count = 2,
        take = true
    }, {
        name = "herb_oregano",
        count = 1,
        take = true
    }, {
        name = "vaso_vinagre",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Bizcocho de limón",
    Desc = "1x Limón, 1x Azúcar, 1x Harina, 1x Yogurt, 1x Huevo, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "bizcocho_limon",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "yogurt",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 6
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Flan de huevo",
    Desc = "2x Huevo, 1x Leche, 1x Azúcar, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "flan",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Hamburguesa",
    Desc = "1x Pan, 1x Carne de ganadera, 1x Lechuga, 1x Tomate, 1x Cuña de queso, 1x Parrilla (↺)",
    Reward = {{
        name = "hamburguesa",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "bread",
        count = 1,
        take = true
    }, {
        name = "carne_calidad",
        count = 1,
        take = true
    }, {
        name = "lettuce",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 1,
        take = true
    }, {
        name = "consumable_cheese_wedge",
        count = 1,
        take = true
    }, {
        name = "parrilla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pastel de zanahoria",
    Desc = "1x Mantequilla, 1x Azúcar, 1x Harina, 2x Huevo, 3x Zanahoria, 1x Leche, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pastel_zanahoria",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "consumable_carrot",
        count = 3,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 7
-------------------------------------------------

-- {
--     TakeItems = true,
--     CurrencyType = 0,
--     Location = 0,
--     Animation = "CocinaTier3",
--     Category = "CocinaTier3",
--     Text = "Hornada de galletas de chocolate (8)",
--     Desc = "1x Harina, 1x Chocolate negro, 1x Huevo, 2x Cacahuetes, 1x Mantequilla, 1x Bandeja de horno (↺)",
--     Reward = {{
--         name = "galleta_chocolate",
--         count = 8
--     }},
--     Minlvl = 7,
--     UseCurrencyMode = false,
--     Job = 0,
--     Type = "item",
--     Items = {{
--         name = "harina",
--         count = 1,
--         take = true
--     }, {
--         name = "consumable_chocolate_negro",
--         count = 1,
--         take = true
--     }, {
--         name = "huevo",
--         count = 1,
--         take = true
--     }, {
--         name = "cacahuetes",
--         count = 2,
--         take = true
--     }, {
--         name = "mantequilla",
--         count = 1,
--         take = true
--     }, {
--         name = "bandeja_horno",
--         count = 1,
--         take = false
--     }}
-- },
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Huevos con jamón",
    Desc = "1x Patata, 1x Jamón curado, 2x Huevo, 1x Sartén (↺)",
    Reward = {{
        name = "huevos_con_jamon",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "patata",
        count = 1,
        take = true
    }, {
        name = "jamon_serrano",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Macedonia",
    Desc = "1x Fresa, 1x Naranja, 1x Arándano, 1x Mora, 1x Melocotón, 1x Azúcar",
    Reward = {{
        name = "macedonia",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "strawberrie",
        count = 1,
        take = true
    }, {
        name = "naranja",
        count = 1,
        take = true
    }, {
        name = "blueberry",
        count = 1,
        take = true
    }, {
        name = "herb_black_berry",
        count = 1,
        take = true
    }, {
        name = "consumable_peach",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }}
},

-------------------------------------------------
-- NIVEL 8
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Pescado con verduras",
    Desc = "1x Pescado, 1x Lechuga, 1x Zanahoria, 1x Guisantes, 1x Pepino, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "pescado_verduras",
        count = 1
    }, {
        name = "fishoil",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "lettuce",
        count = 1,
        take = true
    }, {
        name = "consumable_carrot",
        count = 1,
        take = true
    }, {
        name = "guisantes",
        count = 1,
        take = true
    }, {
        name = "pepino",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Sopa de cebolla",
    Desc = "1x Cebolla, 1x Ajo, 1x Mantequilla, 1x Vaso de brandy, 1x Olla (↺)",
    Reward = {{
        name = "sopa_cebolla",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "vaso_brandy",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Tomates fritos (4)",
    Desc = "2x Tomate, 1x Huevo, 2x Orégano, 1x Harina, 1x Cuña de queso, 1x Vaso de vinagre, 1x Sartén (↺)",
    Reward = {{
        name = "tomates_fritos",
        count = 4
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "tomato",
        count = 2,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "herb_oregano",
        count = 2,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "consumable_cheese_wedge",
        count = 1,
        take = true
    }, {
        name = "vaso_vinagre",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Café irlandés",
    Desc = "1x Café, 1x Leche, 1x Vaso de whiskey",
    Reward = {{
        name = "cafe_irlandes",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_coffee",
        count = 1,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "vaso_whiskey",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 9
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Hamburguesa de pollo",
    Desc = "1x Carne de ave, 1x Pan de maíz, 1x Lechuga, 1x Tomate, 1x Cebolla, 1x Cuña de queso, 1x Parrilla (↺)",
    Reward = {{
        name = "hamburguesa_pollo",
        count = 1
    }},
    Minlvl = 9,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_ave",
        count = 1,
        take = true
    }, {
        name = "pan_maiz",
        count = 1,
        take = true
    }, {
        name = "lettuce",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "consumable_cheese_wedge",
        count = 1,
        take = true
    }, {
        name = "parrilla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Empanada de pescado",
    Desc = "1x Harina de maíz, 1x Pescado, 1x Huevo, 1x Cebolla, 1x Tomate, 1x Bandeja de horno (↺)",
    Reward = {{
        name = "empanada_pescado",
        count = 1
    }},
    Minlvl = 9,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "harina_maiz",
        count = 1,
        take = true
    }, {
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 1,
        take = true
    }, {
        name = "bandeja_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 10
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Marisco al vino",
    Desc = "1x Carne de crustaceo, 1x Vaso de vino, 1x Mantequilla, 1x Ajo, 1x Olla (↺)",
    Reward = {{
        name = "marisco_vino",
        count = 1
    }},
    Minlvl = 10,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_crustaceo",
        count = 1,
        take = true
    }, {
        name = "vaso_vino",
        count = 1,
        take = true
    }, {
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Salteado de setas y verdura",
    Desc = "1x Brócoli, 1x Zanahoria, 2x Hongo parasol, 1x Ajo, 1x Agua, 1x Guisantes, 1x Sartén (↺)",
    Reward = {{
        name = "setas_verduras",
        count = 1
    }},
    Minlvl = 10,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "broccoli",
        count = 1,
        take = true
    }, {
        name = "consumable_carrot",
        count = 1,
        take = true
    }, {
        name = "herb_parasol_mushroom",
        count = 2,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "guisantes",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaTier3",
    Text = "Sopa de tortuga",
    Desc = "2x Carne correosa, 1x Mantequilla, 1x Cebolla, 2x Tomate, 1x Huevo de caimán, 1x Olla (↺)",
    Reward = {{
        name = "sopa_tortuga",
        count = 1
    }},
    Minlvl = 10,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_correosa",
        count = 2,
        take = true
    }, {
        name = "mantequilla",
        count = 1,
        take = true
    }, {
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "tomato",
        count = 2,
        take = true
    }, {
        name = "huevo_caiman",
        count = 1,
        take = true
    }, {
        name = "olla",
        count = 1,
        take = false
    }}
},
}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.CocinaTier3) do
    table.insert(Config.Crafting, item)
end
