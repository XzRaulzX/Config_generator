Config.Establo = {
-------------------------------------------------
-- NIVEL 0
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Documentación de caballo",
    Desc = "1x Nota de papel, 1x Pluma",
    Reward = {{
        name = "HorseTag",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "nota",
        count = 1,
        take = true
    },
    {
        name = "pluma",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Herraduras",
    Desc = "4x Lingote de Hierro",
    Reward = {{
        name = "Horse_Shoe",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "iron",
        count = 4,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Caballete básico",
    Desc = "4x Madera blanda, 4x Madera dura, 3x Palo",
    Reward = {{
        name = "silla_montar_1",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "wood",
        count = 4,
        take = true
    },{
        name = "hwood",
        count = 4,
        take = true
    },
    {
        name = "stick",
        count = 3,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Caballete normal",
    Desc = "4x Madera blanda, 4x Madera dura, 3x Palo, 3x Cobre",
    Reward = {{
        name = "silla_montar_2",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "wood",
        count = 4,
        take = true
    },{
        name = "hwood",
        count = 4,
        take = true
    },
    {
        name = "stick",
        count = 3,
        take = true
    },
    {
        name = "cobre",
        count = 3,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Caballete elegante",
    Desc = "4x Madera blanda, 4x Madera dura, 3x Palo, 3x Cobre, 2x Bronce",
    Reward = {{
        name = "silla_montar_3",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "wood",
        count = 4,
        take = true
    },{
        name = "hwood",
        count = 4,
        take = true
    },
    {
        name = "stick",
        count = 3,
        take = true
    },
    {
        name = "cobre",
        count = 3,
        take = true
    },
    {
        name = "bronce",
        count = 2,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Cepillo de herradura",
    Desc = "3x Madera dura, 1x Hierro, 2x Cobre",
    Reward = {{
        name = "cepillo_herradura",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "hwood",
        count = 3,
        take = true
    },
    {
        name = "iron",
        count = 1,
        take = true
    },
    {
        name = "cobre",
        count = 2,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Cepillo equino",
    Desc = "3x Madera blanda, 3x Pluma",
    Reward = {{
        name = "horsebrush",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "wood",
        count = 3,
        take = true
    },
    {
        name = "pluma",
        count = 3,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Cubo de heno",
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
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Establo",
    Text = "Inyección para caballo",
    Desc = "1x Vaso de Aguardiente, 1x Hierro",
    Reward = {{
        name = "Heal_For_Horse",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "vaso_moonshine",
        count = 1,
        take = true
    }, {
        name = "iron",
        count = 1,
        take = true
    }}
},
-------------------------------------------------
}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.Establo) do
    table.insert(Config.Crafting, item)
end
