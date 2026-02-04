Config.Agricultor = {
-------------------------------------------------
-- NIVEL 0
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Cubito de heno",
    Desc = "5x Trigo",
    Reward = {{
        name = "consumable_haycube",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 5,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = 'craft',
    Category = 'agricultor',
    Text = 'Harina de maíz',
    Desc = '3x Maíz',
    Reward = {{
        name = 'harina_maiz',
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = 'item',
    Items = {{
        name = 'corn',
        count = 3
    }}
},
-------------------------------------------------
-- NIVEL 1
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = 'craft',
    Category = 'agricultor',
    Text = 'Café molido',
    Desc = '5x Granos de Café',
    Reward = {{
        name = 'cafe_molido',
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = 'item',
    Items = {{
        name = 'grano_cafe',
        count = 5
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = 'craft',
    Category = 'agricultor',
    Text = 'Harina',
    Desc = '4x Trigo',
    Reward = {{
        name = 'harina',
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = 'item',
    Items = {{
        name = 'trigo',
        count = 4
    }}
},
-------------------------------------------------
-- NIVEL 2
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de fresas",
    Desc = "4x Fresa, 1x Lata vacía",
    Reward = {{
        name = "consumable_strawberries_can",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "strawberrie",
        count = 4,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de zanahorias",
    Desc = "2x Zanahoria, 1x Lata vacía",
    Reward = {{
        name = "consumable_carrot_can",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_carrot",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de alubias",
    Desc = "3x Alubias, 1x Lata vacía",
    Reward = {{
        name = "lata_alubias",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "alubias",
        count = 3,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 3
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de maíz",
    Desc = "2x Maíz, 1x Lata vacía",
    Reward = {{
        name = "consumable_sweet_corn_can",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "corn",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mermelada de Fresa",
    Desc = "4x Fresa, 1x Agua",
    Reward = {{
        name = "mermelada_fresa",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "strawberrie",
        count = 4,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 4
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de manzanas",
    Desc = "2x Manzana, 1x Lata vacía",
    Reward = {{
        name = "consumable_apple_can",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_apple",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}, 
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mermelada Arándano",
    Desc = "4x Arándano, 1x Agua",
    Reward = {{
        name = "mermelada_arandano",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "blueberry",
        count = 4,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Crema de Cacahuete",
    Desc = "3x Cacahuete, 1x Azúcar",
    Reward = {{
        name = "crema_cacahuete",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cacahuetes",
        count = 3,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 5
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Vinagre",
    Desc = "6x Manzana, 1x Botella vacía",
    Reward = {{
        name = "vinagre",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_apple",
        count = 6,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mermelada de Naranja",
    Desc = "2x Naranja, 1x Agua",
    Reward = {{
        name = "mermelada_naranja",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "naranja",
        count = 2,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Naranjada",
    Desc = "2x Naranja, 1x Azúcar, 1x Canela, 1x Botella vacía",
    Reward = {{
        name = "botella_naranjada",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "naranja",
        count = 2,
        take = true
    }, {
        name = "sugar", 
        count = 1,
        take = true
    }, {
        name = "canela",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 6
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de naranjas",
    Desc = "2x Naranja, 1x Lata vacía",
    Reward = {{
        name = "consumable_orange_can",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "naranja",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mermelada de Mora",
    Desc = "4x Mora, 1x Agua",
    Reward = {{
        name = "mermelada_mora",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "herb_black_berry",
        count = 4,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Pepinillos en vinagre (4)",
    Desc = "2x Pepino, 3x Vaso de vinagre",
    Reward = {{
        name = "pepinillos_vinagre",
        count = 4
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pepino",
        count = 2,
        take = true
    }, {
        name = "vaso_vinagre",
        count = 3,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 7
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mosto de Uva",
    Desc = "10x Uvas, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "mosto_uva",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "uvas",
        count = 10,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Limonada",
    Desc = "2x Limón, 1x Azúcar, 1x Menta, 1x Botella vacía",
    Reward = {{
        name = "botella_limonada",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "limon",
        count = 2,
        take = true
    }, {
        name = "sugar", 
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Tableta de chocolate con leche",
    Desc = "1x Cacao, 1x Leche, 1x Molde de horno (↺)",
    Reward = {{
        name = "consumable_chocolate_bar",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cacao",
        count = 1,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "molde_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 8
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Mermelada de Melocotón",
    Desc = "2x Melocotón, 1x Agua",
    Reward = {{
        name = "mermelada_melocoton",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_peach",
        count = 2,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Tableta de chocolate negro",
    Desc = "3x Cacao, 1x Molde de horno (↺)",
    Reward = {{
        name = "consumable_chocolate_negro",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cacao",
        count = 3,
        take = true
    }, {
        name = "molde_horno",
        count = 1,
        take = false
    }}
},
-------------------------------------------------
-- NIVEL 9
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de melocotones",
    Desc = "2x Melocotón, 1x Lata vacía",
    Reward = {{
        name = "consumable_peach_can",
        count = 1
    }},
    Minlvl = 9,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_peach",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "agricultor",
    Text = "Lata de Macedonia",
    Desc = "1x Manzana, 1x Fresa, 1x Mora, 1x Arándano, 1x Lata vacía",
    Reward = {{
        name = "lata_macedonia",
        count = 1
    }},
    Minlvl = 9,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_apple",
        count = 1,
        take = true
    }, {
        name = "strawberrie",
        count = 1,
        take = true
    }, {
        name = "herb_black_berry",
        count = 1,
        take = true
    }, {
        name = "blueberry",
        count = 1,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
},  
}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.Agricultor) do
    table.insert(Config.Crafting, item)
end
