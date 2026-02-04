Config.Medicos = { -------------------------------------------------
-- NIVEL 0
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Aguja e hilo (5)",
    Desc = "1x Hierro, 1x Fibra",
    Reward = {{
        name = "aguja_hilo",
        count = 5
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "iron",
        count = 1,
        take = true
    }, {
        name = "fibers",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Cataplasma simple",
    Desc = "1x Tela, 1x Salvia",
    Reward = {{
        name = "cataplasma_simple",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "trozotela",
        count = 1,
        take = true
    }, {
        name = "herb_red_sage",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Extracto de menta",
    Desc = "2x Menta, 1x Botella",
    Reward = {{
        name = "extracto_menta",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_wild_mint",
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
    Animation = "craft",
    Category = "Medico",
    Text = "x5 Venda simple (A)",
    Desc = "2x Algodón, 1x Fibra",
    Reward = {{
        name = "venda_medica",
        count = 5
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "cotton",
        count = 2,
        take = true
    }, {
        name = "fibers",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "x5 Venda simple (B)",
    Desc = "2x Tela, 1x Fibra",
    Reward = {{
        name = "venda_medica",
        count = 5
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "trozotela",
        count = 2,
        take = true
    }, {
        name = "fibers",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Ungüento de Enea (Caballos)",
    Desc = "2x Enea, 1x Ginseng de Alaska, 1x Agua",
    Reward = {{
        name = "unguento_enea",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_common_bullrush",
        count = 2,
        take = true
    }, {
        name = "herb_alaskan_ginseng",
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
    Animation = "craft",
    Category = "Medico",
    Text = "Antídoto de Serpiente",
    Desc = "2x Veneno, 1x Bardana",
    Reward = {{
        name = "antidoto_serpiente",
        count = 1
    }},
    Minlvl = 0,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "veneno_serpiente",
        count = 2,
        take = true
    }, {
        name = "herb_burdock_root",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 1
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Sopa de Huesos con Salvia",
    Desc = "1x Carne, 1x Salvia, 1x Agua, 1x Sal",
    Reward = {{
        name = "sopa_huesos_salvia",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "carne",
        count = 1,
        take = true
    }, {
        name = "herb_red_sage",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "salitre",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Cataplasma de Romero y Miel",
    Desc = "1x Romero, 1x Miel, 1x Manteca, 1x Venda",
    Reward = {{
        name = "cataplasma_romero_miel",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "romero",
        count = 1,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }, {
        name = "manteca",
        count = 1,
        take = true
    }, {
        name = "venda_medica",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Té de Avena y Menta",
    Desc = "1x Avena, 1x Menta, 1x Agua, 1x Taza",
    Reward = {{
        name = "te_avena_menta",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "avena",
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }, {
        name = "water",
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
    Animation = "craft",
    Category = "Medico",
    Text = "Agua de Frutas del Bosque",
    Desc = "1x Mora, 1x Arándano, 1x Agua",
    Reward = {{
        name = "agua_frutas_bosque",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_black_berry",
        count = 1,
        take = true
    }, {
        name = "blueberry",
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
    Animation = "craft",
    Category = "Medico",
    Text = "Alcohol destilado",
    Desc = "1x Botella de Aguardiente, 1x Carbón, 1x Botella",
    Reward = {{
        name = "alcohol_destilado",
        count = 5
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "vaso_moonshine",
        count = 1,
        take = true
    }, {
        name = "coal",
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
    Category = "Medico",
    Text = "Inyección para caballo (Med)",
    Desc = "1x Vaso de Aguardiente, 1x Hierro",
    Reward = {{
        name = "Heal_For_Horse",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
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
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Vendas para mascotas",
    Desc = "1x Vaso de Aguardiente, 1x Tela",
    Reward = {{
        name = "pets_bandage",
        count = 1
    }},
    Minlvl = 1,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "vaso_moonshine",
        count = 1,
        take = true
    }, {
        name = "trozotela",
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
    Category = "Medico",
    Text = "Tratamiento para las abejas (2)",
    Desc = "1x Enea, 1x Tomillo, 1x Salvia, 1x Menta",
    Reward = {{
        name = "cura_abejas",
        count = 2
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_common_bullrush",
        count = 1,
        take = true
    }, {
        name = "thyme",
        count = 1,
        take = true
    }, {
        name = "herb_red_sage",
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }}
},
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Elixir de Corteza de Sauce",
    Desc = "1x Corteza de árbol, 1x Alcohol, 1x Lavanda",
    Reward = {{
        name = "elixir_corteza_sauce",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "corteza",
        count = 1,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }, {
        name = "lavanda",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Frasco de pastillas de Linaza",
    Desc = "1x Aceite de Linaza, 1x Harina, 1x Miel",
    Reward = {{
        name = "bote_pastillas",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "aceite_linaza",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Aceite de linaza",
    Desc = "2x Lino, 1x Alcohol Destilado, 1x Botella",
    Reward = {{
        name = "aceite_linaza",
        count = 1
    }},
    Minlvl = 2,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "lino",
        count = 2,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 3
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tónico de Ginseng Silvestre",
    Desc = "1x Ginseng de Alaska, 1x Agua, 1x Limón, 1x Taza",
    Reward = {{
        name = "tonico_ginseng_silvestre",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_alaskan_ginseng",
        count = 1,
        take = true
    }, {
        name = "water",
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
    Animation = "craft",
    Category = "Medico",
    Text = "Bálsamo de Resina y Laurel",
    Desc = "1x Cera, 1x Laurel, 1x Milenrama, 1x Manteca",
    Reward = {{
        name = "balsamo_resina_laurel",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "cera",
        count = 1,
        take = true
    }, {
        name = "herb_oleander_sage",
        count = 1,
        take = true
    }, {
        name = "yarrow",
        count = 1,
        take = true
    }, {
        name = "manteca",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 4
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Brebaje de viento negro",
    Desc = "1x Botella, 1x Ginseng Americano, 1x Vino, 1x Miel",
    Reward = {{
        name = "brebaje_viento_negro",
        count = 4
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "botella",
        count = 1,
        take = true
    }, {
        name = "herb_american_ginseng",
        count = 1,
        take = true
    }, {
        name = "vino",
        count = 1,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tónico de Cuartos Traseros",
    Desc = "1x Vinagre, 1x Romero, 1x Ajo, 1x Zanahoria",
    Reward = {{
        name = "tonico_cuartos_traseros",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "vinagre",
        count = 1,
        take = true
    }, {
        name = "romero",
        count = 1,
        take = true
    }, {
        name = "garlic",
        count = 1,
        take = true
    }, {
        name = "consumable_carrot",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Bálsamo para heridas de mascotas",
    Desc = "1x Manteca, 1x Venda, 1x Avena, 1x Milenrama",
    Reward = {{
        name = "balsamo_mascotas",
        count = 1
    }},
    Minlvl = 4,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "manteca",
        count = 1,
        take = true
    }, {
        name = "venda_medica",
        count = 1,
        take = true
    }, {
        name = "avena",
        count = 1,
        take = true
    }, {
        name = "yarrow",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 5
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tintura de Ajenjo",
    Desc = "1x Ajenjo, 1x Alcohol, 2x Botella",
    Reward = {{
        name = "tintura_ajenjo",
        count = 2
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "ajenjo",
        count = 1,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 2,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tónico de Piel y Pulmón",
    Desc = "1x Corteza de árbol, 1x Agua, 1x Limón, 1x Miel",
    Reward = {{
        name = "tonico_piel_pulmon",
        count = 1
    }},
    Minlvl = 5,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "corteza",
        count = 1,
        take = true
    }, {
        name = "water",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 6
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Recontituyente de Emergencia",
    Desc = "2x Agua, 1x Miel, 1x Sal, 1x Limón, 1x Cecina",
    Reward = {{
        name = "recontituyente_emergencia",
        count = 5
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "water",
        count = 2,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }, {
        name = "salitre",
        count = 1,
        take = true
    }, {
        name = "limon",
        count = 1,
        take = true
    }, {
        name = "cecina",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tónico de Sangre Cocida",
    Desc = "1x Carne correosa, 1x Laurel, 1x Manteca, 1x Venda",
    Reward = {{
        name = "tonico_sangre_cocida",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "carne_correosa",
        count = 1,
        take = true
    }, {
        name = "herb_oleander_sage",
        count = 1,
        take = true
    }, {
        name = "manteca",
        count = 1,
        take = true
    }, {
        name = "venda_medica",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tintura de Valeriana Negra",
    Desc = "1x Valeriana, 1x Alcohol, 1x Lavanda",
    Reward = {{
        name = "tintura_valeriana_negra",
        count = 1
    }},
    Minlvl = 6,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "valeriana",
        count = 1,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }, {
        name = "lavanda",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 7
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Elixir de cedro plateado",
    Desc = "1x Corteza de árbol, 1x Ginseng de Alaska, 1x Miel, 1x Alcohol",
    Reward = {{
        name = "elixir_cedro_plateado",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "corteza",
        count = 1,
        take = true
    }, {
        name = "herb_alaskan_ginseng",
        count = 1,
        take = true
    }, {
        name = "miel",
        count = 1,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }}
}, {
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Píldora de extracto de salvia",
    Desc = "1x Salvia, 1x Harina, 1x Menta, 1x Vinagre",
    Reward = {{
        name = "pildora_extracto_salvia",
        count = 1
    }},
    Minlvl = 7,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "herb_red_sage",
        count = 1,
        take = true
    }, {
        name = "harina",
        count = 1,
        take = true
    }, {
        name = "herb_wild_mint",
        count = 1,
        take = true
    }, {
        name = "vinagre",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 8
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Tónico del viejo mundo",
    Desc = "1x Vino, 2x Ginseng americano, 2x Ginseng alaskeño, 1x Romero",
    Reward = {{
        name = "tonico_viejo_mundo",
        count = 1
    }},
    Minlvl = 8,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "vino",
        count = 1,
        take = true
    }, {
        name = "herb_american_ginseng",
        count = 2,
        take = true
    }, {
        name = "herb_alaskan_ginseng",
        count = 2,
        take = true
    }, {
        name = "romero",
        count = 1,
        take = true
    }}
}, -------------------------------------------------
-- NIVEL 9
-------------------------------------------------
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Medico",
    Text = "Jeringuilla (5)",
    Desc = "1x Hierro, 1x Botella, 10x Matricaria, 1x Alcohol destilado",
    Reward = {{
        name = "syringe",
        count = 5
    }},
    Minlvl = 9,
    UseCurrencyMode = false,
    Job = {"medicoAR", "medicoBW", "medicoMF"},
    Type = "item",
    Items = {{
        name = "iron",
        count = 1,
        take = true
    }, {
        name = "botella",
        count = 1,
        take = true
    }, {
        name = "herb_wild_feverfew",
        count = 10,
        take = true
    }, {
        name = "alcohol_destilado",
        count = 1,
        take = true
    }}
}}

-- Agregamos a la configuración general los items de artesano
for _, item in pairs(Config.Medicos) do
    table.insert(Config.Crafting, item)
end
