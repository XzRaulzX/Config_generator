Usables = {}

-- Inicializar Usables.items si no existe
if not Usables.items then
    Usables.items = {}
end

Usables.itemsLHR = {
    -- -------------------------------------------------------
    --  BEBIDAS
    -- -------------------------------------------------------
    ["bebida_queso"] = {
        name = "Bebida de queso",
        hunger = 10.0,
        thirst = 20.0,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["batido_chocolate"] = {
        name = "Batido de chocolate",
        hunger = 10.0,
        thirst = 20.0,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["batido_fresa"] = {
        name = "Batido de fresa",
        hunger = 5.0,
        thirst = 20.0,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    -- ["cocacola"] = {
    --     name = "Lally Cola",
    --     hunger = 0,
    --     thirst = 20,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 3
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },
    ["consumable_milk"] = {
        name = "Botella de leche",
        hunger = 14.4,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["consumable_cabra"] = {
        name = "Vaso de leche de cabra",
        hunger = 12,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["miel"] = {
        name = "Miel",
        hunger = 11.5,
        thirst = 5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },	
    ["pepsi"] = {
        name = "Swift",
        hunger = 0,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 3
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },	
    ["water"] = {
        name = "Agua",
        hunger = 0,
        thirst = 15,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 2
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },		
    ["yogurt"] = {
        name = "Bote de yogurt",
        hunger = 17.2,
        thirst = 7.5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },	
    -- ["yogurt_arandanos"] = {
    --     name = "Bote de yogurt de arándanos",
    --     hunger = 17.2,
    --     thirst = 7.5,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 0
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },	
    ["yogurt_dulce"] = {
        name = "Bote de yogurt dulce",
        hunger = 20.1,
        thirst = 10,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },	
    ["yogurt_fresa"] = {
        name = "Bote de yogurt de fresa",
        hunger = 17.2,
        thirst = 7.5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["yogurt_melocoton"] = {
        name = "Bote de yogurt de melocotón",
        hunger = 17.2,
        thirst = 7.5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["yogurt_mora"] = {
        name = "Bote de yogurt de mora",
        hunger = 17.2,
        thirst = 7.5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["zarzaparrilla"] = {
        name = "Zarzaparrilla",
        hunger = 0,
        thirst = 30,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 15
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    -- ["zumo_manzana"] = {
    --     name = "Zumo de manzana",
    --     hunger = 0,
    --     thirst = 25,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 4
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },
    -- ["zumo_naranja"] = {
    --     name = "Zumo de naranja",
    --     hunger = 0,
    --     thirst = 25,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 4
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },
    -- ["zumo_limon_menta"] = {
    --     name = "Zumo de limón y menta",
    --     hunger = 0,
    --     thirst = 17.5,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 0
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },
    ["vaso_mosto"] = {
        name = "Vaso de mosto",
        hunger = 5.8,
        thirst = 18.5,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["vaso_naranjada"] = {
        name = "Vaso de naranjada",
        hunger = 5.8,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["vaso_limonada"] = {
        name = "Vaso de limonada",
        hunger = 5.8,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["leche_merengada"] = {
        name = "Leche merengada",
        hunger = 23.0,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "drink"
        },
        returnItems = {{
            name = "botella",
            amount = 1
        }}
    },	
    -- ["granizado_sandia"] = {
    --     name = "Granizado de sandía",
    --     hunger = 11.5,
    --     thirst = 17.5,
    --     stress = 0,
    --     tempModifier = {
    --         value = -5,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 0
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },
    ["lally_fresa"] = {
        name = "Lally Fresa",
        hunger = 0,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 3
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["vaso_ponche_huevo"] = {
        name = "Vaso de ponche con huevo",
        hunger = 16,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 3
        },
        effects = {
            enabled = true,
            animationName = "drink"
        }
    },
    ["agua_con_gas"] = {
        name = "Agua con gas",
        hunger = 0,
        thirst = 23,
        stress = 0,
        tempModifier = {
            value = 0,
            duration = 25000
        },
        player = {
            staminaCore = 2
        },
        effects = {
            enabled = true,
            animationName = "drink"
        },
        returnItems = {{
            name = "botella",
            amount = 1
        }}
    },
    ["chocolate_taza"] = {
        name = "Chocolate a la taza",
        hunger = 5.8,
        thirst = 20,
        stress = 0,
        tempModifier = {
            value = 5,
            duration = 25000
        },
        player = {
            staminaCore = 0
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["consumable_coffee"] = {
        name = "Café",
        hunger = 0,
        thirst = 17.5,
        stress = -10,
        tempModifier = {
            value = 5,
            duration = 25000
        },
        player = {
            staminaCore = 10
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["cafe_irlandes"] = {
        name = "Café irlandés",
        hunger = 5.8,
        thirst = 12,
        stress = -10,
        tempModifier = {
            value = 5,
            duration = 25000
        },
        player = {
            staminaCore = 5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["infusion_ginseng"] = {
        name = "Infusión de ginseng americano",
        hunger = 0,
        thirst = 25,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 6
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["infusion_milenrama"] = {
        name = "Infusión de milenrama",
        hunger = 0,
        thirst = 20,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 6
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["infusion_tomillo"] = {
        name = "Infusión de tomillo",
        hunger = 0,
        thirst = 25,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 6
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["te_conleche"] = {
        name = "Té con leche",
        hunger = 0,
        thirst = 25,
        stress = -5,
        tempModifier = {
            value = 4,
            duration = 25000
        },
        player = {
            staminaCore = 2.5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["te_feliz"] = {
        name = "Té con alcohol",
        hunger = 0,
        thirst = 25,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["te_negro"] = {
        name = "Té negro",
        hunger = 0,
        thirst = 12.5,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 2.5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["te_verde"] = {
        name = "Té verde",
        hunger = 0,
        thirst = 12.5,
        stress = -5,
        tempModifier = {
            value = 3,
            duration = 25000
        },
        player = {
            staminaCore = 2.5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    -- ["cafe_helado"] = {
    --     name = "Cafe con helado",
    --     hunger = 17.2,
    --     thirst = 20,
    --     stress = 0,
    --     tempModifier = {
    --         value = -3,
    --         duration = 25000
    --     },
    --     player = {
    --         staminaCore = 2.5
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "coffee"
    --     },
    --     returnItems = {{
    --         name = "taza_vacia",
    --         amount = 1
    --     }}
    -- },
    
    -- ["agua_frutas_bosque"] = {
    --     name = "Agua de frutas del bosque",
    --     hunger = 11.5,
    --     thirst = 25,
    --     stress = 0,
    --     tempModifier = {
    --         value = 0,
    --         duration = 25000
    --     },
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "drink"
    --     }
    -- },

    -- -------------------------------------------------------
    --  COMIDA
    -- -------------------------------------------------------
    -- alitas	Alitas de pollo	200	0	0	0	eat	
    ["alitas"]        = {
        name = "Alitas de pollo",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	

    ["pepino"]        = {
        name = "Pepino",
        hunger = 3.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	

    ["pepinillo_vinagre"]        = {
        name = "Pepinillo en vinagre",
        hunger = 5.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	

    ["huevo_vinagre"]        = {
        name = "Huevo en vinagre",
        hunger = 8.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- ancas_rana_menta	Ancas de rana con menta	250	0	0	0	eat	
    ["ancas_rana_menta"]        = {
        name = "Ancas de rana con menta",
        hunger = 20.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- ancas_rana_tomillo	Ancas de rana con tomillo	200	0	0	0	eat	
    -- ["ancas_rana_tomillo"]        = {
    --     name = "Ancas de rana con tomillo",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- blueberry	Arándano	50	0	0	0	eat	
    ["blueberry"]        = {
        name = "Arándano",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BLACKBERRY01X"
        }
    },	
    ["baya"]        = {
        name = "Baya",
        hunger = 2.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BLACKBERRY01X"
        }
    },	
    ["cacahuetes"]        = {
        name = "Cacahuete",
        hunger = 2.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BLACKBERRY01X"
        }
    },	
    ["crema_cacahuete"]        = {
        name = "Crema de cacahuete",
        hunger = 14.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    ["uvas"]        = {
        name = "Uvas",
        hunger = 4.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BLACKBERRY01X"
        }
    },
    -- -- bocadillo_condimentado	Bocadillo de carne con condimentos	275	0	0	0	eat	
    -- ["bocadillo_condimentado"]        = {
    --     name = "Bocadillo de carne con condimentos",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- bocadillo_pollo	Bocadillo de Pollo y Queso	250	0	0	0	eat	
    -- ["bocadillo_pollo"]        = {
    --     name = "Bocadillo de pollo y queso",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- bread	Pan	50	0	0	0	eat	
    ["bread"]        = {
        name = "Pan",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- carne_ave_cocinada	Carne de ave cocinada	150	0	0	0	eat	
    ["carne_ave_cocinada"]        = {
        name = "Carne de ave cocinada",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "p_redefleshymeat01xb"
        }
    },
    -- carne_ave_tomillo	Carne de ave con tomillo	250	0	0	0	eat	
    ["carne_ave_tomillo"]        = {
        name = "Carne de ave con tomillo",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- carne_ave_menta	Carne de ave con menta	250	0	0	0	eat	
    -- ["carne_ave_menta"]        = {
    --     name = "Carne de ave con menta",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },		
    -- carne_calidad_oregano	Carne cocinada de gran calidad con oregano	300	0	0	0	eat
    ["carne_calidad_oregano"]        = {
        name = "Carne cocinada de gran calidad con oregano",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- carne_calidad_oregano	Carne cocinada de gran calidad con oregano	300	0	0	0	eat
    ["chicharron"]        = {
        name = "Chicharrón",
        hunger = 20.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },			
    -- carne_calidad_tomillo	Carne cocinada de gran calidad con tomillo	300	0	0	0	eat
    -- ["carne_calidad_tomillo"]        = {
    --     name = "Carne cocinada de gran calidad con tomillo",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- carne_cocinada	Carne cocinada	150	0	0	0	eat	
    ["carne_cocinada"]        = {
        name = "Carne cocinada",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "p_redefleshymeat01xb"
        }
    },	
    -- carne_correosa_cocinada	Carne correosa cocinada	150	0	0	0	eat
    ["carne_correosa_cocinada"]        = {
        name = "Carne correosa cocinada",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "p_redefleshymeat01xb"
        }
    },		
    -- carne_correosa_menta	Carne correosa con menta	250	0	0	0	eat	
    -- ["carne_correosa_menta"]        = {
    --     name = "Carne correosa con menta",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- carne_correosa_tomillo	Carne correosa con tomillo	200	0	0	0	eat	
    ["carne_correosa_tomillo"]        = {
        name = "Carne correosa con tomillo",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- cecina	Cecina	200	0	0	0	eat	
    ["cecina"]        = {
        name = "Cecina",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- churros	Churros	150	0	0	0	eat	
    -- ["churros"]        = {
    --     name = "Churros",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    ["cacao_canela"] = {
        name = "Cacao con leche y canela",
        hunger = 8.6,
        thirst = 17.5,
        stress = 0,
        tempModifier = {
            value = 5,
            duration = 25000
        },
        player = {
            staminaCore = 5
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
        returnItems = {{
            name = "taza_vacia",
            amount = 1
        }}
    },
    ["bollo_canela"] = {
        name = "Bollo de canela",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_apple	Manzana	75	0	0	0	eat
    ["consumable_apple"]        = {
        name = "Manzana",
        hunger = 8.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["cebolla"]        = {
        name = "Cebolla",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_ONIONWHITE_01X"
        }
    },	
    -- consumable_candy_bag	Bolsa de caramelos	50	0	0	0	eat	
    ["consumable_candy_bag"]        = {
        name = "Bolsa de caramelos",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_carrot	Zanahoria	50	0	0	0	eat	
    ["consumable_carrot"]        = {
        name = "Zanahoria",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_cheese_wedge	Cuña de queso	150	0	0	0	eat	
    ["consumable_cheese_wedge"]        = {
        name = "Cuña de queso",
        hunger = 6.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_cheese_wedge	Cuña de queso de cabra	150	0	0	0	eat	
    ["cuna_quesocabra"]        = {
        name = "Cuña de queso de cabra",
        hunger = 7.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_chocolate_bar	Tableta de chocolate con leche	125	0	0	0	eat	
    ["consumable_chocolate_bar"]        = {
        name = "Tableta de chocolate con leche",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_corn	Maíz Cocido	120	0	0	0	eat	
    ["consumable_corn"]        = {
        name = "Maíz cocido",
        hunger = 13.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_crackers	Galleta saladas	60	0	0	0	eat	
    ["consumable_crackers"]        = {
        name = "Galleta saladas",
        hunger = 6.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- consumable_peach	Melocotón	55	30	0	0	eat	
    ["consumable_peach"]        = {
        name = "Melocotón",
        hunger = 6.3,
        thirst = 3,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- croissant	Croissant	225	0	0	0	eat	
    ["croissant"]        = {
        name = "Croissant",
        hunger = 14.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- donut	Donut	125	0	0	0	eat	
    -- ["donut"]        = {
    --     name = "Donut",
    --     hunger = 14.4,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- ensalada_pasta	Pasta con ensalada	300	0	0	0	eat
    ["ensalada"]        = {
        name = "Ensalada",
        hunger = 18.7,
        thirst = 8,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    ["rebanada_mermelada"]        = {
        name = "Rebanada de pan con mermelada",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- ["ensalada_pasta"]        = {
    --     name = "Pasta con ensalada",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },		
    -- galleta	Galleta	70	0	0	0	eat	
    ["galleta"]        = {
        name = "Galleta",
        hunger = 8.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- galleta	Galleta	70	0	0	0	eat	
    ["galleta_chocolate"]        = {
        name = "Galleta de chocolate",
        hunger = 13.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- hamburguesa	Hamburguesa de carne	300	0	0	0	eat	
    ["hamburguesa"]        = {
        name = "Hamburguesa de carne",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- hamburguesa_pollo	Hamburguesa de pollo	275	0	0	0	eat	
    ["hamburguesa_pollo"]        = {
        name = "Hamburguesa de pollo",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- herb_black_berry	Mora	50	0	0	0	eat	
    ["herb_black_berry"]        = {
        name = "Mora",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- huevos_salmuera	Huevos en salmuera	75	0	0	0	eat	
    -- ["huevos_salmuera"]        = {
    --     name = "Huevos en salmuera",
    --     hunger = 86.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eatCan",
    --         prop = "s_canbeans01x"
    --     }
    -- },
    -- jamon_dulce	Lata jamón dulce	300	0	0	0	eat	
    ["jamon_dulce"]        = {
        name = "Lonchas de jamón dulce",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- jamon_serrano	Lonchas de jamón serrano	200	0	0	0	eat	
    ["jamon_serrano"]        = {
        name = "Lonchas de jamón curado",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- lata_macedonia	Lata de Macedonia	300	175	0	0	eat	
    ["lata_macedonia"]        = {
        name = "Lata de Macedonia",
        hunger = 34.5,
        thirst = 17.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },

    ["lata_alubias"]        = {
        name = "Lata de alubias",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },

    ["alubias_guisadas"]        = {
        name = "Alubias guisadas",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    ["alubias_huevo"]        = {
        name = "Alubias, salchicha y huevo",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    -- lata_macedonia	Lata de Macedonia	300	175	0	0	eat	
    ["macedonia"]        = {
        name = "Macedonia",
        hunger = 23.0,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- magdalena_frutos	Magdalena de frutos rojos	200	0	0	0	eat	
    ["magdalena_frutos"]        = {
        name = "Magdalena de frutos rojos",
        hunger = 11.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- manzana_caramelo	Manzana de caramelo	150	0	0	0	eat	
    ["manzana_caramelo"]        = {
        name = "Manzana de caramelo",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- manzana_vino	Manzanas al vino tinto	300	0	0	0	eat
    ["manzana_vino"]        = {
        name = "Manzanas al vino tinto",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- mermelada_arandano	Mermelada de Arándano	250	0	0	0	eat	
    ["mermelada_arandano"]        = {
        name = "Mermelada de arándano",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- mermelada_fresa	Mermelada de Fresa	250	0	0	0	eat	
    ["mermelada_fresa"]        = {
        name = "Mermelada de fresa",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- mermelada_melocoton	Mermelada de Melocotón	250	0	0	0	eat	
    ["mermelada_melocoton"]        = {
        name = "Mermelada de melocotón",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- mermelada_mora	Mermelada de Mora	250	0	0	0	eat	
    ["mermelada_mora"]        = {
        name = "Mermelada de mora",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- mermelada_naranja	Mermelada de Naranja	250	0	0	0	eat	
    ["mermelada_naranja"]        = {
        name = "Mermelada de naranja",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- naranja	Naranja	75	50	0	0	eat	
    ["naranja"]        = {
        name = "Naranja",
        hunger = 8.6,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["blackcurrant"]        = {
        name = "Arándano negro",
        hunger = 3.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["blueberry"]        = {
        name = "Arándano",
        hunger = 2.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["lettuce"]        = {
        name = "Lechuga",
        hunger = 4.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_LETTUCE01X"
        }
    },
    -- palomitasdul	Palomitas dulces	200	0	0	0	eat	
    -- ["palomitasdul"]        = {
    --     name = "Palomitas dulces",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- palomitasman	Palomitas con mantequilla	200	0	0	0	eat	
    -- ["palomitasman"]        = {
    --     name = "Palomitas con mantequilla",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- pastel_chocolate	Pastel de chocolate	250	0	0	0	eat	
    ["porcion_pastel_chocolate"]        = {
        name = "Pastel de chocolate",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pastel_fresa	Pastel de fresa	250	0	0	0	eat	
    ["porcion_pastel_fresa"]        = {
        name = "Pastel de fresa",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pastel_manzana	Pastel de manzana	250	0	0	0	eat	
    ["porcion_pastel_manzana"]        = {
        name = "Pastel de manzana",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pastel_queso	Pastel de queso	250	0	0	0	eat	
    ["porcion_pastel_queso"]        = {
        name = "Pastel de queso",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pastel_zanahoria	Pastel de zanahoria	250	0	0	0	eat	
    ["porcion_pastel_zanahoria"]        = {
        name = "Pastel de zanahoria",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- pastel_blueberry	Pastel de arándanos	250	0	0	0	eat	
    ["porcion_pastel_arandano"]        = {
        name = "Pastel de arándanos",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pastel_mora	Pastel de mora	250	0	0	0	eat
    ["porcion_pastel_mora"]        = {
        name = "Pastel de mora",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- pastel_melocoton	Pastel de melocotón	250	0	0	0	eat	
    ["porcion_pastel_melocoton"]        = {
        name = "Pastel de melocotón",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    
    ["porcion_bizcocho_limon"]        = {
        name = "Bizcocho de limón",
        hunger = 10.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["porcion_bizcocho_naranja"]        = {
        name = "Bizcocho de naranja",
        hunger = 10.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["porcion_bizcocho_yogurt"]        = {
        name = "Bizcocho de yogurt",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },

    -- patata_horno	Patatas horneada	200	0	0	0	eat	
    ["patata_horno"]        = {
        name = "Patatas horneadas",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- patatas_fritas	Patatas fritas	150	0	0	0	eat
    -- ["patatas_fritas"]        = {
    --     name = "Patatas fritas",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- perrito	Perrito caliente	250	0	0	0	eat	
    -- ["perrito"]        = {
    --     name = "Perrito caliente",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- pescado_cocinado	Pescado cocinado	150	0	0	0	eat	
    ["pescado_cocinado"]        = {
        name = "Pescado cocinado",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- pescado_guarnicion	Pescado Menière	200	0	0	0	eat	
    -- ["pescado_guarnicion"]        = {
    --     name = "Pescado Menière",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- pescado_horno	Pescado al horno	300	0	0	0	eat	
    ["pescado_horno"]        = {
        name = "Pescado al horno",
        hunger = 26.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- pescado_menta	Pescado con menta	225	0	0	0	eat	
    -- ["pescado_menta"]        = {
    --     name = "Pescado con menta",
    --     hunger = 25.9,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- pescado_oregano	Pescado con orégano	225	0	0	0	eat	
    -- ["pescado_oregano"]        = {
    --     name = "Pescado con orégano",
    --     hunger = 25.9,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- pescado_relleno	Pescado relleno	250	0	0	0	eat	
    -- ["pescado_menta"]        = {
    --     name = "Pescado con menta",
    --     hunger = 25.9,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    ["pescado_relleno"]        = {
        name = "Pescado relleno",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- pescado_verduras	Pescado con verduras	250	0	0	0	eat	
    ["pescado_verduras"]        = {
        name = "Pescado con verduras",
        hunger = 29.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["huevos_con_jamon"]        = {
        name = "Huevos con jamón",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- trozo_chorizo	Porción de pizza	275	0	0	0	eat	
    -- ["trozo_chorizo"]        = {
    --     name = "Porción de pizza",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- trozo_tomate	Porción de pizza	250	0	0	0	eat	
    -- ["trozo_tomate"]        = {
    --     name = "Porción de pizza",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- -- pollo_cerveza	Pollo a la cerveza	300	0	0	0	eat	
    -- ["pollo_cerveza"]        = {
    --     name = "Pollo a la cerveza",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- pollo_frito	Pollo frito	175	0	0	0	eat	
    ["pollo_frito"]        = {
        name = "Pollo frito",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- -- pollo_relleno	Pollo relleno	400	0	0	0	eat	
    -- ["pollo_relleno"]        = {
    --     name = "Pollo relleno",
    --     hunger = 46.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- queso	Cuña de queso	300	0	0	0	eat
    -- ["queso"]        = {
    --     name = "Cuña de queso",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- quesocabra	Cuña de queso de cabra	150	0	0	0	eat	
    ["quesocabra"]        = {
        name = "Cuña de queso de cabra",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- regaliz	Regaliz dulce	150	0	0	0	eat	
    -- ["regaliz"]        = {
    --     name = "Regaliz dulce",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- sandwich	Sandwich	225	0	0	0	eat	
    ["medio_sandwich"]        = {
        name = "Medio sandwich",
        hunger = 17.2,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["morcilla"]        = {
        name = "Morcilla",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["pastel_morcilla"]        = {
        name = "Pastel de morcilla",
        hunger = 27.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["cottage"]        = {
        name = "Cottage pie",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    ["tomates_fritos"]        = {
        name = "Tomates fritos",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    -- anca_cocinada	Ancas de rana cocinadas	125	0	0	0	eat	
    ["anca_cocinada"]        = {
        name = "Ancas de rana cocinadas",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- strawberrie	Fresa	50	0	0	0	eat	
    ["strawberrie"]        = {
        name = "Fresa",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- tortitas_miel	Tortitas con miel	150	0	0	0	eat	
    -- ["tortitas_miel"]        = {
    --     name = "Tortitas con miel",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- trozo_nupcial	Trozo de tarta nupcial	200	0	0	0	eat	
    ["trozo_nupcial"]        = {
        name = "Trozo de tarta nupcial",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- aros_cebolla	Aros de cebolla	200	0	0	0	eat	
    ["aros_cebolla"]        = {
        name = "Aros de cebolla",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- cigarro_chocolate	Cigarrillo de chocolate	100	0	0	0	eat	
    ["cigarro_chocolate"]        = {
        name = "Cigarrillo de chocolate",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- helado_chocolate	Helado de chocolate	175	150	0	0	eat	
    -- ["helado_chocolate"]        = {
    --     name = "Helado de chocolate",
    --     hunger = 17.2,
    --     thirst = 10,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     tempModifier = {
    --         value = -5,
    --         duration = 25000
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- -- helado_crema	Helado de crema	150	100	0	0	eat	
    ["helado_crema"]        = {
        name = "Helado de crema",
        hunger = 17.2,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        tempModifier = {
            value = -5,
            duration = 25000
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- -- helado_fresa	Helado de fresa	175	150	0	0	eat	
    -- ["helado_fresa"]        = {
    --     name = "Helado de fresa",
    --     hunger = 17.2,
    --     thirst = 10,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     tempModifier = {
    --         value = -5,
    --         duration = 25000
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- -- -- helado_galleta	Helado con galleta	175	150	0	0	eat	
    -- ["helado_galleta"]        = {
    --     name = "Helado con galleta",
    --     hunger = 17.2,
    --     thirst = 10,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     tempModifier = {
    --         value = -5,
    --         duration = 25000
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- galleta_jengibre	Galleta de jengibre	80	0	0	0	eat	
    -- ["galleta_jengibre"]        = {
    --     name = "Galleta de jengibre",
    --     hunger = 9.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- tartaleta_merengue	Tartaleta de merengue	200	0	0	0	eat	
    ["tartaleta_merengue"]        = {
        name = "Tartaleta de merengue",
        hunger = 13.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- flan	Flan de huevo	250	0	0	0	eat	
    ["flan"]        = {
        name = "Flan de huevo",
        hunger = 20.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- croissant_mermelada	Croissant con mermelada	200	0	0	0	eat	
    -- ["croissant_mermelada"]        = {
    --     name = "Croissant con mermelada",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- tostadas_mermelada	Tostadas con mermelada	150	0	0	0	eat	
    -- ["tostadas_mermelada"]        = {
    --     name = "Tostadas con mermelada",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- tostadas_mantequilla	Tostadas con mantequilla	150	0	0	0	eat	
    -- ["tostadas_mantequilla"]        = {
    --     name = "Tostadas con mantequilla",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- tostadas_quesocabra	Tostadas con queso	175	0	0	0	eat
    -- ["tostadas_quesocabra"]        = {
    --     name = "Tostadas con queso de cabra",
    --     hunger = 20.1,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },	
    -- canape_mermelada	Canapé dulce	125	0	0	0	eat	
    -- ["canape_mermelada"]        = {
    --     name = "Canapé con mermelada",
    --     hunger = 14.4,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- -- canape_queso	Canapé de queso	125	0	0	0	eat	
    -- ["canape_queso"]        = {
    --     name = "Canapé de queso",
    --     hunger = 14.4,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- waffles_miel	Waffles	150	0	0	0	eat	
    -- ["waffles_miel"]        = {
    --     name = "Waffles",
    --     hunger = 17.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- pretzel	Pretzel	175	0	0	0	eat	
    -- ["pretzel"]        = {
    --     name = "Pretzel",
    --     hunger = 20.1,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- pan_queso_ajo	Pan de ajo y queso	250	0	0	0	eat	
    -- ["pan_queso_ajo"]        = {
    --     name = "Pan de ajo y queso",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- muffins_brocoli	Muffin de brócoli	275	0	0	0	eat	
    -- ["muffins_brocoli"]        = {
    --     name = "Muffin de brócoli",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- scones_zanahoria	Scones de zanahoria	125	0	0	0	eat	
    -- ["scones_zanahoria"]        = {
    --     name = "Scones de zanahoria",
    --     hunger = 14.4,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- oblea	Oblea	10	0	0	0	eat	
    ["oblea"]        = {
        name = "Oblea",
        hunger = 1.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- bombon	Bombón	70	0	0	0	eat
    ["bombon"]        = {
        name = "Bombón",
        hunger = 5.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["magdalena"]        = {
        name = "Magdalena",
        hunger = 13.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["leche_frita"]        = {
        name = "Leche frita",
        hunger = 15.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    ["arroz_leche"]        = {
        name = "Arroz con leche",
        hunger = 25.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["helado_cafe"]        = {
        name = "Café helado",
        hunger = 11.0,
        thirst = 17.0,
        stress = 0,
        tempModifier = {
            value = -3,
            duration = 25000
        },
        effects = {
            enabled = true,
            animationName = "coffee"
        },
    },	
    ["natillas"]        = {
        name = "Natillas",
        hunger = 20.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pan_especias"]        = {
        name = "Pan de especias",
        hunger = 18.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["compota_manzana"]        = {
        name = "Compota de manzana",
        hunger = 20.0,
        thirst = 10.0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["napolitana_chocolate"]        = {
        name = "Napolitana de chocolate",
        hunger = 22.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["tiramisu"]        = {
        name = "Tiramisú",
        hunger = 25.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },

    -- huevas_pez	Huevas de pez esturión	155	0	0	0	eat	
    -- ["huevas_pez"]        = {
    --     name = "Huevas de pez esturión",
    --     hunger = 17.8,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eatCan",
    --         prop = "s_canbeans01x"
    --     }
    -- },	
    -- lata_caviar	Lata de caviar	175	0	0	0	eat	
    ["lata_caviar"]        = {
        name = "Lata de caviar",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },		
    -- canape_caviar	Canapé de caviar	190	0	0	0	eat	
    -- ["canape_caviar"]        = {
    --     name = "Canapé de caviar",
    --     hunger = 21.8,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- pan_maiz	Pan de maíz	125	0	0	0	eat	
    ["pan_maiz"]        = {
        name = "Pan de maíz",
        hunger = 9.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- pan_especiado	Pan especiado	150	0	0	0	eat	
    ["pan_especiado"]        = {
        name = "Pan especiado",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- empanada_carne	Empanada de carne	250	0	0	0	eat	
    ["empanada_carne"]        = {
        name = "Empanada de carne",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["empanada_pescado"]        = {
        name = "Empanada de pescado",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["guiso_casero"]        = {
        name = "Guiso casero",
        hunger = 23.0,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- salchichon	Salchichón	250	0	0	0	eat	
    ["salchichon"]        = {
        name = "Salchichón",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- salchicha	Salchicha	175	0	0	0	eat	
    ["salchicha"]        = {
        name = "Salchicha",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- trozo_melon	Rodaja de melón	80	65	0	0	eat	
    ["trozo_melon"]        = {
        name = "Rodaja de melón",
        hunger = 9.2,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["tomato"]        = {
        name = "Tomate",
        hunger = 3.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "S_TOMATO01X"
        }
    },
    -- trozo_sandia	Rodaja de sandía	95	50	0	0	eat	
    ["trozo_sandia"]        = {
        name = "Rodaja de sandía",
        hunger = 10.9,
        thirst = 6.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- melon_jamon	Aperitivo de melón con jamón	150	50	0	0	eat	
    ["melon_jamon"]        = {
        name = "Aperitivo de melón con jamón",
        hunger = 17.2,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- crustaceo_cocinado	Crustáceo cocinado	150	0	0	0	eat	
    ["crustaceo_cocinado"]        = {
        name = "Crustáceo cocinado",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    -- brioche_relleno	Brioche relleno	250	0	0	0	eat	
    -- ["brioche_relleno"]        = {
    --     name = "Brioche relleno",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- quiche	Quiche	250	0	0	0	eat	
    -- ["quiche"]        = {
    --     name = "Quiche",
    --     hunger = 28.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eat",
    --         prop = "P_BREAD05X"
    --     }
    -- },
    -- ancas_can	Ancas de rana en lata	250	0	0	0	stew
    ["ancas_can"]        = {
        name = "Ancas de rana en lata",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },		
    -- albondigas	Albondigas con tómate	350	0	0	0	stew	
    ["albondigas"]        = {
        name = "Albondigas con tómate",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- carne_calidad_menta	Carne cocinada de gran calidad con menta	350	0	0	0	stew	
    ["carne_calidad_menta"]        = {
        name = "Carne cocinada de gran calidad con menta",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["patata_horno"]        = {
        name = "Patata horneada",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["patata_rellena"]        = {
        name = "Patata rellena",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- carne_can	Carne en lata	200	0	0	0	stew	
    ["carne_can"]        = {
        name = "Carne en lata",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- carne_salsa	Carne en salsa de frutos rojos	400	0	0	0	stew	
    -- ["carne_salsa"]        = {
    --     name = "Carne en salsa de frutos rojos",
    --     hunger = 46.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- carne_tomillo	Carne cocinada con tomillo	250	0	0	0	stew
    ["carne_tomillo"]        = {
        name = "Carne cocinada con tomillo",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },		
    -- carne_calidad_can	Carne de calidad en lata	250	0	0	0	stew
    ["carne_calidad_can"]        = {
        name = "Carne de calidad en lata",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },		
    -- cebolla_asada	Cebolla asada	200	0	0	0	stew	
    ["cebolla_asada"]        = {
        name = "Cebolla asada",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- cebolla_rellena	Cebolla rellena	275	0	0	0	stew
    ["cebolla_rellena"]        = {
        name = "Cebolla rellena",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    ["carne_calidad_oregano"]        = {
        name = "Carne de calidad con orégano",
        hunger = 25.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    ["emparedado_salchicha"]        = {
        name = "Emparedado de salchicha",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    -- consumable_apple_can	Lata de manzanas	185	125	0	0	stew
    ["consumable_apple_can"]        = {
        name = "Lata de manzanas",
        hunger = 21.3,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },		
    -- consumable_carrot_can	Lata de zanahorias	100	50	0	0	stew
    ["consumable_carrot_can"]        = {
        name = "Lata de zanahorias",
        hunger = 11.5,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- consumable_orange_can	Lata de naranjas	185	125	0	0	stew
    ["consumable_orange_can"]        = {
        name = "Lata de naranjas",
        hunger = 21.3,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- consumable_peach_can	Lata de melocotones	185	125	0	0	stew	
    ["consumable_peach_can"]        = {
        name = "Lata de melocotones",
        hunger = 21.3,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- consumable_salmon_can	Salmon Can	300	50	0	0	stew
    -- ["consumable_salmon_can"]        = {
    --     name = "Lata de salmón",
    --     hunger = 34.5,
    --     thirst = 5,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eatCan",
    --         prop = "s_canbeans01x"
    --     }
    -- },	
    -- consumable_strawberries_can	Lata de fresas	185	125	0	0	stew	
    ["consumable_strawberries_can"]        = {
        name = "Lata de fresas",
        hunger = 21.3,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- consumable_sweet_corn_can	Lata de maíz dulce	185	125	0	0	stew
    ["consumable_sweet_corn_can"]        = {
        name = "Lata de maíz dulce",
        hunger = 21.3,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- correosa_can	Carne correosa en lata	200	0	0	0	stew	
    ["correosa_can"]        = {
        name = "Carne correosa en lata",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- croquetas	Croquetas	200	0	0	0	stew
    -- ["croquetas"]        = {
    --     name = "Croquetas",
    --     hunger = 23.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- ensalada_salmon	Ensalada de salmón	300	0	0	0	stew	
    -- ["ensalada_salmon"]        = {
    --     name = "Ensalada de salmón",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- espagueti	Spaguetti	350	0	0	0	stew	
    -- ["espagueti"]        = {
    --     name = "Espagueti",
    --     hunger = 40.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- estofado_carne	Estofado de carne	200	0	0	0	stew	
    ["estofado_carne"]        = {
        name = "Estofado de carne",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    ["rebanada_cacahuete"]        = {
        name = "Rebanada de pan con crema de cacahuete",
        hunger = 17.2,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- guiso_calidad_alta_condimentado	Guiso de alta calidad	300	100	0	0	stew	
    -- ["guiso_calidad_alta_condimentado"]        = {
    --     name = "Guiso de alta calidad condimentado",
    --     hunger = 34.5,
    --     thirst = 10,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- guiso_calidad_baja	Guiso de calidad baja	150	50	0	0	stew	
    ["guiso_calidad_baja"]        = {
        name = "Guiso de baja calidad",
        hunger = 17.2,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- -- guiso_calidad_baja_condimentado	Guiso de baja calidad	200	75	0	0	stew
    -- ["guiso_calidad_baja_condimentado"]        = {
    --     name = "Guiso de baja calidad condimentado",
    --     hunger = 23.0,
    --     thirst = 7.5,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },		
    -- guiso_calidad_media_condimentado	Guiso de calidad media	225	75	0	0	stew
    -- ["guiso_calidad_media_condimentado"]        = {
    --     name = "Guiso de calidad media condimentado",
    --     hunger = 25.9,
    --     thirst = 7.5,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- guiso_guarma	Guiso de guarma	275	50	0	0	stew	
    ["guiso_guarma"]        = {
        name = "Guiso de Guarma",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- guiso_guarma_condimentado	Guiso de Guarma	300	100	0	0	stew	
    -- ["guiso_guarma_condimentado"]        = {
    --     name = "Guiso de Guarma condimentado",
    --     hunger = 34.5,
    --     thirst = 10,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- guiso_pescado	Guiso de pescado	250	200	0	0	stew	
    ["guiso_pescado"]        = {
        name = "Guiso de pescado",
        hunger = 28.7,
        thirst = 7.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- huevos_fritos	Huevos fritos	200	0	0	0	stew
    -- ["huevos_fritos"]        = {
    --     name = "Huevos fritos",
    --     hunger = 20.7,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- huevos_rotos	Huevos rotos	275	0	0	0	stew	
    -- ["huevos_rotos"]        = {
    --     name = "Huevos rotos",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- trozo_lasagna	Porción de lasagna	175	0	0	0	stew	
    -- ["trozo_lasagna"]        = {
    --     name = "Porción de lasagna",
    --     hunger = 20.1,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- lata_cocido	Lata de cocido	250	0	0	0	stew	
    ["lata_cocido"]        = {
        name = "Lata de cocido",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- lata_estofado	Lata de estofado	250	0	0	0	stew	
    ["lata_estofado"]        = {
        name = "Lata de estofado",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- macarroni	Macarroni	350	0	0	0	stew
    ["macarroni"]        = {
        name = "Macarroni",
        hunger = 40.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- marisco_vino	Marisco al vino	400	0	0	0	stew
    ["marisco_vino"]        = {
        name = "Marisco al vino",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },		
    -- ratatouille	Ratatouille 	350	0	0	0	stew
    -- ["ratatouille"]        = {
    --     name = "Ratatouille",
    --     hunger = 40.2,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- salmon_horno	Salmón al horno	400	0	0	0	stew	
    -- ["salmon_horno"]        = {
    --     name = "Salmón al horno",
    --     hunger = 46.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },
    -- setas_verduras	Setas con verduras	250	0	0	0	stew
    ["setas_verduras"]        = {
        name = "Setas con verduras",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- sopa_cebolla	Sopa de cebolla	150	250	0	0	stew	
    ["sopa_cebolla"]        = {
        name = "Sopa de cebolla",
        hunger = 23.0,
        thirst = 11.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- sopa_maiz	Sopa de maíz	200	100	0	0	stew	
    ["sopa_maiz"]        = {
        name = "Sopa de maíz",
        hunger = 17.2,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["budin"]        = {
        name = "Budín negro",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["rebanada_miel"]        = {
        name = "Rebanada pan con miel",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- sopa_pollo	Sopa de pollo	250	200	0	0	stew	
    ["sopa_pollo"]        = {
        name = "Sopa de pollo",
        hunger = 28.7,
        thirst = 20,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- sopa_tortuga	Sopa de tortuga	350	225	0	0	stew
    ["sopa_tortuga"]        = {
        name = "Sopa de tortuga",
        hunger = 25.9,
        thirst = 12,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- sopa_verduras	Sopa de verduras	250	150	0	0	stew
    ["sopa_verduras"]        = {
        name = "Sopa de verduras",
        hunger = 20.7,
        thirst = 7.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },		
    -- sopa_pescado	Sopa de pescado	180	80	0	0	stew
    ["sopa_pescado"]        = {
        name = "Sopa de pescado",
        hunger = 21.8,
        thirst = 5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- tarro_visceras	Tarro de vísceras	175	10	0	0	stew	
    ["tarro_visceras"]        = {
        name = "Tarro de vísceras",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },
    -- -- tortellini	Plato de Tortellini	400	0	0	0	stew
    -- ["tortellini"]        = {
    --     name = "Plato de Tortellini",
    --     hunger = 46.0,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- carne_menta	Carne cocinada con menta	250	0	0	0	stew	
    ["carne_menta"]        = {
        name = "Carne cocinada con menta",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- carne_oregano	Carne cocinada con orégano	250	0	0	0	stew
    ["carne_oregano"]        = {
        name = "Carne cocinada con orégano",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- arroz_cocido	Arroz cocido	200	0	0	0	stew
    ["arroz_cocido"]        = {
        name = "Arroz cocido",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	
    -- risotto	Risotto con setas	300	0	0	0	stew	
    -- ["risotto"]        = {
    --     name = "Risotto con setas",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- ensalada_frutas	Ensalada de frutas	275	0	0	0	stew	
    -- ["ensalada_frutas"]        = {
    --     name = "Ensalada de frutas",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- sachichas_pure	Salchichas con puré de patata	275	0	0	0	stew
    -- ["sachichas_pure"]        = {
    --     name = "Salchichas con puré de patata",
    --     hunger = 31.6,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- plato_spezzatino	Guiso Spezzatino	285	0	0	0	stew
    -- ["plato_spezzatino"]        = {
    --     name = "Guiso Spezzatino",
    --     hunger = 32.8,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "stew",
    --     }
    -- },	
    -- crustaceo_can	Lata de crustáceo	250	0	0	0	stew	
    ["crustaceo_can"]        = {
        name = "Lata de crustáceo",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },	
    -- conserva_lago	Conserva del lago	300	0	0	0	stew
    -- ["conserva_lago"]        = {
    --     name = "Conserva del lago",
    --     hunger = 34.5,
    --     thirst = 0,
    --     stress = 0,
    --     player = {
    --         healthCore = 0,
    --     },
    --     effects = {
    --         enabled = true,
    --         animationName = "eatCan",
    --         prop = "s_canbeans01x"
    --     }
    -- },	
    -- surstromming	Surströmming	285	0	0	0	stew	
    ["surstromming"]        = {
        name = "Surströmming",
        hunger = 32.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eatCan",
            prop = "s_canbeans01x"
        }
    },

    ["setas_verduras"]        = {
        name = "Salteado de setas y verdura",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },	

    ["tortilla_maiz"]        = {
        name = "Tortilla de maíz",
        hunger = 5.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["tamal"]        = {
        name = "Tamal",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["taco"]        = {
        name = "Taco",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },	
    ["carne_nortena"]        = {
        name = "Carne asada norteña",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["chimichanga"]        = {
        name = "Chimichanga",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["chiles_nogada"]        = {
        name = "Chiles en nogada",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["tlayudas"]        = {
        name = "Tlayuda",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["huevos_rancheros"]        = {
        name = "Huevos rancheros",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["pozole"]        = {
        name = "Pozole",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["carnitas"]        = {
        name = "Carnitas",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["pescado_veracruzana"]        = {
        name = "Pescado a la veracruzana",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["sopa_azteca"]        = {
        name = "Sopa azteca",
        hunger = 34.5,
        thirst = 17.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["mazorca_asada"]        = {
        name = "Mazorca asada",
        hunger = 11.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["dirty_rice"]        = {
        name = "Dirty rice",
        hunger = 20.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pure_salchicha"]        = {
        name = "Puré de patata y salchicha",
        hunger = 20.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pollo_frito"]        = {
        name = "Pollo frito",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["estofado_tomate"]        = {
        name = "Estofado de tomate con pan de maíz",
        hunger = 23.0,
        thirst = 8,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["cangrejo_frito"]        = {
        name = "Cangrejo frito",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["bagre_frito"]        = {
        name = "Bagre frito",
        hunger = 25.3,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["hoppin_jhonn"]        = {
        name = "Hoppin Jhonn",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["gumbo"]        = {
        name = "Gumbo",
        hunger = 25.9,
        thirst = 12,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["jambalaya"]        = {
        name = "Jambalaya",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["husspuppies"]        = {
        name = "Husspuppies",
        hunger = 25.9,
        thirst = 12,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["guandul"]        = {
        name = "Guandul",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pasta_cruda"]        = {
        name = "Pasta Cruda",
        hunger = 28.7,
        thirst = -10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["cerdo_agridulce"]        = {
        name = "Cerdo agridulce",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["arroz_frito"]        = {
        name = "Arroz frito con huevo",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["chop_suey"]        = {
        name = "Chop Suey",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["rollito_primavera"]        = {
        name = "Rollito de primavera",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["zongzi"]        = {
        name = "Zongzi",
        hunger = 17.2,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["sopa-wongton"]        = {
        name = "Sopa Wongton",
        hunger = 23.0,
        thirst = 12.5,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["wanton"]        = {
        name = "Wanton mee",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pollo_gong"]        = {
        name = "Pollo gong bao",
        hunger = 25.9,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pato_laqueado"]        = {
        name = "Pato laqueado",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["chow_mein"]        = {
        name = "Chow mein",
        hunger = 28.7,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pastel_luna"]        = {
        name = "Pastel de luna",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["stotty"]        = {
        name = "Stotty",
        hunger = 14.4,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["ploughman_lunch"]        = {
        name = "Ploughman's Lunch",
        hunger = 21.8,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["fish_chips"]        = {
        name = "Fish and chips",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["jam_roly_poly"]        = {
        name = "Jam Roly-Poly",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["kedgeree"]        = {
        name = "Kedgeree",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pudding"]        = {
        name = "Yorkshire pudding",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["hotpot"]        = {
        name = "Lancashire hotpot",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["welsh_rarebit"]        = {
        name = "Welsh rarebit",
        hunger = 20.1,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["wellington"]        = {
        name = "Wellington",
        hunger = 34.5,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["cornish"]        = {
        name = "Cornish Pasties",
        hunger = 31.6,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["gachas"]        = {
        name = "Gachas",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["emparedado_cecina"]        = {
        name = "Emparedado de cecina",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["estofado_bufalo"] = {
        name = "Estofado de búfalo",
        hunger = 28.7,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["papilla_maiz"] = {
        name = "Papilla de maíz",
        hunger = 20.7,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "eat",
            prop = "P_BREAD05X"
        }
    },
    ["sopa_hermanas"] = {
        name = "Sopa de las tres hermanas",
        hunger = 21.8,
        thirst = 10,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    ["pemmican"] = {
        name = "Pemmican",
        hunger = 23.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    -- judia_perdiz
    ["judias_perdiz"] = {
        name = "Judías con perdiz",
        hunger = 18.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- venado_arandano
    ["venado_arandano"] = {
        name = "Venado con arándanos",
        hunger = 20.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- trucha_jamon
    ["trucha_jamon"] = {
        name = "Trucha con jamón",
        hunger = 20.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- conejo_pure
    ["conejo_pure"] = {
        name = "Conejo con puré de patata",
        hunger = 20.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- cangrejo_picante
    ["cangrejo_picante"] = {
        name = "Cangrejos picantes",
        hunger = 22.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- plato_montanes
    ["plato_montanes"] = {
        name = "Plato montañés",
        hunger = 26.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- guiso_setas
    ["guiso_setas"] = {
        name = "Guiso de setas",
        hunger = 25.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- empanada_anguila
    ["empanada_anguila"] = {
        name = "Empanada de anguila",
        hunger = 25.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- cazuela_cacao
    ["cazuela_cacao"] = {
        name = "Cazuela con cacao",
        hunger = 26.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- estofado_caza
    ["estofado_caza"] = {
        name = "Estofado de caza",
        hunger = 22.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },
    -- codorniz_escabeche
    ["codorniz_escabeche"] = {
        name = "Codorniz en escabeche",
        hunger = 29.0,
        thirst = 0,
        stress = 0,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "stew",
        }
    },

    --- ANTÍDOTO
    ["antidoto_serpiente"] = {
        name = "Antídoto de serpiente",
        hunger = 0,
        thirst = 0,
        stress = -30,
        player = {
            healthCore = 0,
        },
        effects = {
            enabled = true,
            animationName = "medicine",
        },
        ClientAction = function()
            TriggerEvent('bln_hud:UseAntidote')     -- Snake poison cure
        end,
    },
    
}

for k, v in pairs(Usables.itemsLHR) do
    Usables.items[k] = v
end