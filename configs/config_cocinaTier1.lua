Config.CocinaTier1 = {{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "CocinaTier1",
    Text = "Ancas de rana cocinadas",
    Desc = "1x Ancas de rana, 1x Sartén (↺)",
    Reward = {{
        name = "anca_cocinada",
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
        name = "sarten",
        count = 1,
        take = false
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Taza de café (2)",
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
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Pan (2)(H)",
    Desc = "1x Agua, 1x Trigo",
    Reward = {{
        name = "bread",
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
        name = "trigo",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Carne cocinada",
    Desc = "1x Carne", -- , 1x Sartén (↺)",
    Reward = {{
        name = "carne_cocinada",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne",
        count = 1,
        take = true
    }, 
    -- {
    --     name = "sarten",
    --     count = 1,
    --     take = false
    -- }
}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Carne correosa cocinada",
    Desc = "1x Carne correosa, 1x Sartén (↺)",
    Reward = {{
        name = "carne_correosa_cocinada",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_correosa",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Carne correosa con tomillo",
    Desc = "1x Carne correosa, 2x Tomillo, 1x Sartén",
    Reward = {{
        name = "carne_correosa_tomillo",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_correosa",
        count = 1,
        take = true
    }, {
        name = "thyme",
        count = 2,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Cebolla asada",
    Desc = "1x Cebolla, 1x Tomillo",
    Reward = {{
        name = "cebolla_asada",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "cebolla",
        count = 1,
        take = true
    }, {
        name = "thyme",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Carne de ave cocinada",
    Desc = "1x Carne de ave, 1x Sartén (↺)",
    Reward = {{
        name = "carne_ave_cocinada",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "carne_ave",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "knifecooking",
    Category = "CocinaTier1",
    Text = "Pescado cocinado",
    Desc = "1x Pescado, 1x Sartén (↺)",
    Reward = {{
        name = "pescado_cocinado",
        count = 1
    },
    {
        name = "fishoil",
        count = 1,
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "sarten",
        count = 1,
        take = false
    }}
}}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.CocinaTier1) do
    table.insert(Config.Crafting, item)
end
