Config.Pescadero = {{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Ancas de rana enlatada",
    Desc = "2x Ancas de rana, 1x Lata vacía",
    Reward = {{
        name = "ancas_can",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "ancas_rana",
        count = 2,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Huevas de pez esturión",
    Desc = "2x Pescado, 1x Navaja (↺)",
    Reward = {{
        name = "huevas_pez",
        count = 1
    }, {
        name = "fishoil",
        count = 1,
        take = true
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 2,
        take = true
    }, {
        name = "navaja",
        count = 1,
        take = false
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Lata de caviar",
    Desc = "1x Huevas de pez esturión, 1x Lata vacía",
    Reward = {{
        name = "lata_caviar",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "huevas_pez",
        count = 1,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Salmon enlatado",
    Desc = "1x Pescado, 1x Lata vacía",
    Reward = {{
        name = "consumable_salmon_can",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Surströmming", -- NUEVO
    Desc = "1x Pescado, 1x Agua, 1x Ajo",
    Reward = {{
        name = "surstromming",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Crustáceo enlatado", -- NUEVO
    Desc = "1x Crustáceo cocinado, 1x Aceite de pescado, 1x Lata vacía",
    Reward = {{
        name = "crustaceo_can",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "crustaceo_cocinado",
        count = 1,
        take = true
    }, {
        name = "fishoil",
        count = 1,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Pescadero",
    Text = "Conserva del lago", -- NUEVO
    Desc = "1x Pescado cocinado, 1x Crustáceo cocinado, 1x Aceite de pescado, 1x Ajo, 1x Lata vacía",
    Reward = {{
        name = "conserva_lago",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "pescado_cocinado",
        count = 1,
        take = true
    }, {
        name = "crustaceo_cocinado",
        count = 1,
        take = true
    }, {
        name = "fishoil",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "empty_can",
        count = 1,
        take = true
    }}
}}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.Pescadero) do
    table.insert(Config.Crafting, item)
end
