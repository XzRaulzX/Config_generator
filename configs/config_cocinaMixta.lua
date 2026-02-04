Config.CocinaMixta = {{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaMixta",
    Text = "Café dulce",
    Pack = "comun",
    Desc = "1x Agua, 1x Café molido, 2x Taza",
    Reward = {{
        name = "consumable_coffee",
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
        name = "cafe_molido",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 2,
        take = true
    }}
},  {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Infusión de ginseng americano",
    Pack = "comun",
    Desc = "1x Agua, 1x Ginseng Americano, 1x Limon, 1x Taza",
    Reward = {{
        name = "infusion_ginseng",
        count = 1
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
        name = "herb_american_ginseng",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Infusión de tomillo",
    Pack = "comun",
    Desc = "1x Agua, 1x Tomillo, 1x Limon, 1x Taza",
    Reward = {{
        name = "infusion_tomillo",
        count = 1
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
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Pan (2)",
    Pack = "comun",
    Desc = "1x Trigo, 1x Agua",
    Reward = {{
        name = "bread",
        count = 2
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "trigo",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Té con leche",
    Pack = "comun",
    Desc = "1x Té negro, 1x Leche, 1x Taza",
    Reward = {{
        name = "te_conleche",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "te_negro",
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
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Té feliz (2)",
    Pack = "comun",
    Desc = "1x Té negro, 1x Leche, 1x Vaso de cognac, 1x Taza",
    Reward = {{
        name = "te_feliz",
        count = 2
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "te_negro",
        count = 1,
        take = true
    }, {
        name = "consumable_milk",
        count = 1,
        take = true
    }, {
        name = "vaso_cognac",
        count = 1,
        take = true
    }, {
        name = "taza_vacia",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Zumo de manzana",
    Desc = "1x Azucar, 2x Manzana, 1x Botella",
    Reward = {{
        name = "zumo_manzana",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "consumable_apple",
        count = 2,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "CocinaTier3",
    Category = "CocinaMixta",
    Text = "Zumo de naranja",
    Desc = "1x Azucar, 2x Naranja, 1x Botella",
    Reward = {{
        name = "zumo_naranja",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "sugar",
        count = 1,
        take = true
    }, {
        name = "naranja",
        count = 2,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
}}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.CocinaMixta) do
    table.insert(Config.Crafting, item)
end
