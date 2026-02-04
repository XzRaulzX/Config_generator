Config.Destilador = {
-------------------------------------------------
-- NIVEL 0
-------------------------------------------------  
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Destilador",
    Text = "Aguardiente",
    Desc = "10x Azúcar, 1x Botella vacía",
    Reward = {{
        name = "moonshine",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "sugar",
        count = 10,
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
    Category = "Destilador",
    Text = "Cerveza Rubia",
    Desc = "4x Trigo, 1x Botella vacía, 1x Agua",
    Reward = {{
        name = "beer",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 4,
        take = true
    }, {
        name = "botella",
        count = 1,
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
    Category = "Destilador",
    Text = "Zarzaparrilla",
    Desc = "3x Planta de casis, 1x Botella vacía",
    Reward = {{
        name = "zarzaparrilla",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "herb_black_current",
        count = 3,
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
    Category = "Destilador",
    Text = "Whiskey",
    Desc = "6x Trigo, 1x Botella vacía",
    Reward = {{
        name = "consumable_whiskey",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 6,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
-- NIVEL 1
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Destilador",
    Text = "Cerveza Tostada",
    Desc = "4x Trigo, 1x Botella vacía, 1x Agua, 1x Sartén (↺)",
    Reward = {{
        name = "beer_tostada",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 4,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }, {
        name = "water",
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
    Animation = "craft",
    Category = "Destilador",
    Text = "Agua con gas",
    Desc = "1x Agua, 1x Azúcar, 1x Limón, 1x Botella vacía",
    Reward = {{
        name = "agua_con_gas",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "water",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
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
    Category = "Destilador",
    Text = "Tequila",
    Desc = "4x Ágave, 1x Botella vacía, 1x Agua",
    Reward = {{
        name = "tequila",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "agave",
        count = 4,
        take = true
    }, {
        name = "botella",
        count = 1,
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
    Category = "Destilador",
    Text = "Cerveza Negra",
    Desc = "3x Trigo, 2x Granos de café, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "beer_negra",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 3,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "grano_cafe",
        count = 2,
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
    Category = "Destilador",
    Text = "Vodka",
    Desc = "8x Patata, 2x Azúcar, 1x Botella vacía",
    Reward = {{
        name = "vodka",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "patata",
        count = 8,
        take = true
    }, {
        name = "sugar",
        count = 2,
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
    Category = "Destilador",
    Text = "Sidra",
    Desc = "6x Manzana, 1x Agua, 1x Tomillo, 1x Botella vacía",
    Reward = {{
        name = "sidra",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "consumable_apple",
        count = 6,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "botella",
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
    Category = "Destilador",
    Text = "Cognac",
    Desc = "4x Azúcar, 2x Vaso de guardiente, 1x Botella vacía",
    Reward = {{
        name = "consumable_cognac",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "sugar",
        count = 4,
        take = true
    }, {
        name = "vaso_moonshine",
        count = 2,
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
    Category = "Destilador",
    Text = "Whiskey de Tennessee",
    Desc = "10x Trigo, 2x Milenrama, 1x Botella vacía",
    Reward = {{
        name = "consumable_tenn_whiskey",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 10,
        take = true
    }, {
        name = "yarrow",
        count = 2,
        take = true
    }, {
        name = "botella",
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
    Category = "Destilador",
    Text = "Hidromiel",
    Desc = "5x Agua, 3x Trigo, 2x Miel, 1x Botella vacía",
    Reward = {{
        name = "hidromiel",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "water",
        count = 5,
        take = true
    }, {
        name = "trigo",
        count = 3,
        take = true
    }, {
        name = "miel",
        count = 2,
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
    Category = "Destilador",
    Text = "Ron de Guarma",
    Desc = "6x Azúcar, 1x Agua, 1x Cacao, 1x Botella vacía",
    Reward = {{
        name = "consumable_carib_rum",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "sugar",
        count = 6,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "cacao",
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
    Category = "Destilador",
    Text = "Ginebra Londinense",
    Desc = "3x Naranja, 3x Maíz, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "consumable_londry_gin",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "naranja",
        count = 3,
        take = true
    }, {
        name = "corn",
        count = 3,
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
    Category = "Destilador",
    Text = "Absenta",
    Desc = "4x Ajenjo, 1x Tomillo, 2x Limón, 1x Botella vacía",
    Reward = {{
        name = "absenta",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "ajenjo",
        count = 4,
        take = true
    }, {
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 2,
        take = true
    }, {
        name = "botella",
        count = 1,
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
    Category = "Destilador",
    Text = "Brandy de Cypres",
    Desc = "1x Vaso de vino, 2x Huevos, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "consumable_cyprus_brandy",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "vaso_vino",
        count = 1,
        take = true
    }, {
        name = "huevo",
        count = 2,
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
    Category = "Destilador",
    Text = "Vino",
    Desc = "25x Uva, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "vino",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "uvas",
        count = 25,
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
    Category = "Destilador",
    Text = "Champagne",
    Desc = "15x Uva, 8x Arándano, 8x Mora, 1x Agua, 1x Botella vacía",
    Reward = {{
        name = "champan",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "uvas",
        count = 15,
        take = true
    }, {
        name = "blueberry",
        count = 8,
        take = true
    }, {
        name = "herb_black_berry",
        count = 8,
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





































--        {
--     TakeItems = true,
--     CurrencyType = 0,
--     Location = 0,
--     Animation = "craft",
--     Category = "Destilador",
--     Text = "Nihonshu Japonés",
--     Desc = "3x Arroz, 1x Botella vacía, 1x Azúcar",
--     Reward = {{
--         name = "consumable_nihonshu",
--         count = 1
--     }},
--     Minlvl = 5,
--     UseCurrencyMode = false,
--     Job = 0,
--     Type = "item",
--     Items = {{
--         name = "arroz",
--         count = 3,
--         take = true
--     }, {
--         name = "botella",
--         count = 1,
--         take = true
--     }, {
--         name = "sugar",
--         count = 1,
--         take = true
--     }}
-- },  
-- {
--     TakeItems = true,
--     CurrencyType = 0,
--     Location = 0,
--     Animation = "craft",
--     Category = "Destilador",
--     Text = "Kvas",
--     Desc = "2x Trigo, 2x Agua, 1x Menta",
--     Reward = {{
--         name = "kvas",
--         count = 1
--     }},
--     Minlvl = 3,
--     UseCurrencyMode = false,
--     Job = 0,
--     Type = "item",
--     Items = {{
--         name = "trigo",
--         count = 2,
--         take = true
--     }, {
--         name = "water",
--         count = 2,
--         take = true
--     }, {
--         name = "herb_wild_mint",
--         count = 1,
--         take = true
--     }}
-- },    


}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.Destilador) do
    table.insert(Config.Crafting, item)
end
