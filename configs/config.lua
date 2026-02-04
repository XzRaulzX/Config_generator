Config = {}

Config.defaultlang = "es_lang"

-- Crafting Key
Config.Keys = {
	G = 0x760A9C6F
}

-- Options: s, m, l
Config.Styles = {
	fontSize = 'm',
	descriptionsidebar = true
}

Config.Commands = {
}

-- distance to interact with Locations and campfires
Config.Distances = {
	campfire = 1.5,
	locations = 1.2,
	almacenes = 1.2
}

Config.UsosMaxSarten = math.random(17, 22)

Config.Animations = {
	["craft"] = { --Default Animation
		dict = "mech_inventory@crafting@fallbacks",
		name = "full_craft_and_stow",
		flag = 27,
		type = 'standard'
	},
	["CocinaTier3"] = {
        -- dict = "amb_camp@prop_camp_foodprep@working@seasoning@female_a@base",
        -- name = "seasoning_trans_resting_active_look",
        dict = "amb_camp@prop_camp_foodprep@working@seasoning@male_b@idle_c",
        name = "idle_i",
        flag = 27,
        type = 'standard',
        prop = {
            model = 'P_SALTSHAKER01X',
            coords = {
                x = -0.02,
                y = -0.04,
                z = 0.011,
                xr = 197.0,
                yr = -15.9,
                zr = 77.0
            },
            bone = 'SKEL_R_Finger13'
        }
    },
	["spindlecook"] = {
		dict = "amb_camp@world_camp_fire_cooking@male_d@wip_base",
		name = "wip_base",
		flag = 17,
		type = 'standard',
		prop = {
			model = 'p_stick04x',
			coords = {
				x = 0.2,
				y = 0.04,
				z = 0.12,
				xr = 170.0,
				yr = 50.0,
				zr = 0.0
			},
			bone = 'SKEL_R_Finger13',
			subprop = {
				model = 's_meatbit_chunck_medium01x',
				coords = {
					x = -0.30,
					y = -0.08,
					z = -0.30,
					xr = 0.0,
					yr = 0.0,
					zr = 70.0
				}
			}
		}
	},
	["knifecooking"] = {
		dict = "amb_camp@world_player_fire_cook_knife@male_a@wip_base",
		name = "wip_base",
		flag = 17,
		type = 'standard',
		prop = {
			model = 'w_melee_knife06',
			coords = {
				x = -0.01,
				y = -0.02,
				z = 0.02,
				xr = 190.0,
				yr = 0.0,
				zr = 0.0
			},
			bone = 'SKEL_R_Finger13',
			subprop = {
				model = 'p_redefleshymeat01xa',
				coords = {
					x = 0.00,
					y = 0.02,
					z = -0.20,
					xr = 0.0,
					yr = 0.0,
					zr = 0.0
				}
			}
		}
	},
	["campfire"] = {
		dict = "script_campfire@lighting_fire@male_male",
		name = "light_fire_b_p2_male_b",
		flag = 17,
		type = 'standard'
	}
}

-- Configuración para cargar ubicaciones desde la base de datos
Config.LoadLocationsFromDB = true -- Cambiar a false para usar ubicaciones hardcodeadas

-- {"CocinaTier2":true,"CocinaTier1":true,"Destilador":true,"medico":true,"empty":true,"agricultor":true,"Ganadero":true,"Tabacalero":true,"medico":true,"Artesano":true,"Armero":true}
Config.Categories = {
	{
		ident = 'food',
		text = 'Craft Food',
		desc = 'Comida',
		Location = 0,
		Job = 0
	},
	{
		ident = 'items',
		text = 'Craft Item',
		desc = 'Objetos',
		Location = 0,
		Job = 0
	},
	{
		ident = 'weapons',
		text = 'Weapons',
		desc = 'Armas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'meleeweapons',
		text = 'Melee weapons',
		desc = 'Armas de cuerpo a cuerpo',
		Location = 0,
		Job = 0
	},
	{
		ident = 'cocina',
		text = 'Comida',
		desc = 'Comida',
		Location = 0,
		Job = 0
	},
    {
		ident = 'CocinaDulce',
		text = 'Comida Dulce',
		desc = 'Deliciosas recetas para panaderías y pastelerías',
		Location = 0,
		Job = 0
	},
    {
		ident = 'CocinaMixta',
		text = 'Otros platos y Bebidas',
		desc = 'Recetas de platos y bebidas variadas',
		Location = 0,
		Job = 0
	},
    {
		ident = 'CocinaPacks',
		text = 'Especialidades',
		desc = 'Platos y bebidas de alta gama, aprendidos de grandes profesionales',
		Location = 0,
		Job = 0
	},
	{
		ident = 'CocinaTier3',
		text = 'Comida Avanzada',
		desc = 'La maestría en la cocina',
		Location = 0,
		Job = 0
	},
	{
		ident = 'CocinaTier2',
		text = 'Comida Media',
		desc = 'Recetas de cocina media, de preparación sencilla pero elaboradas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'CocinaTier1',
		text = 'Comida',
		desc = 'Recetas de cocina básica, de fácil preparación',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Destilador',
		text = 'Destilería',
		desc = 'Las mejores recetas de destilados y bebidas espirituosas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Distribuidora',
		text = 'Distribuidora',
		desc = 'Distribuidora de alimentos y bebidas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Medico',
		text = 'Medicina',
		desc = 'Recetas de medicina y curación',
		Location = 0,
		Job = { 'medicoAR', 'medicoBW', 'medicoMF' }
	},
	{
		ident = 'agricultor',
		text = 'Agricultor',
		desc = 'Recetas de agricultura y cosecha',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Ganadero',
		text = 'Ganadero',
		desc = 'Recetas de ganadería y cría de animales',
		Location = 0,
		Job = 0
	},
    {
		ident = 'Pescadero',
		text = 'Pescadero',
		desc = 'Recetas de pesca y preparación de pescado',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Tabacalero',
		text = 'Tabacalero',
		desc = 'Recetas de tabaco y cigarrillos',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Artesano',
		text = 'Artesano',
		desc = 'Recetas de artesanía y fabricación de objetos',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Establo',
		text = 'Establo',
		desc = 'Recetas de útiles para los equinos',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Perista',
		text = 'Perista',
		desc = 'Recetas de orfebrería y fabricación de joyas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'Armero',
		text = 'Armero',
		desc = 'Recetas de fabricación de armas',
		Location = 0,
		Job = 0
	},
	{
		ident = 'empty',
		text = 'Elaboraciones',
		desc = 'Craftear',
		Location = 0,
		Job = 0
	},
	{
		ident = 'MesaHerreroBanda',
		text = 'Mesa de Herrero',
		desc = 'Aquí puedes manipular armas y objetos',
		Location = 0,
		Job = 0
	},
	{
		ident = 'MesaEnfermeriaBanda',
		text = 'Mesa de Enfermería',
		desc = 'Aquí puedes elaborar medicinas y curas',
		Location = 0,
		Job = 0
	},
}

-- Ubicaciones hardcodeadas (se usan si LoadLocationsFromDB = false)
Config.Locations = {
	{
		name = 'Artesano de Valentine',
		id = 'artesanoval',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -369.960,
		y = 802.8258,
		z = 115.99,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Artesano de Strawberry',
		id = 'artesanoSB',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -1817.53,
		y = -426.167,
		z = 160.07,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Artesano de Blackwater',
		id = 'artesanobw',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -878.444,
		y = -1393.20,
		z = 43.749,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Artesano de Saint Denis',
		id = 'artesanosd',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = 2536.879,
		y = -1344.34,
		z = 46.963,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
    {
		name = 'Artesano de Armadillo',
		id = 'artesanoar',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -3684.33,
        y = -2566.18,
        z = -13.55,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = "Artesano de McFarlane",
		id = 'artesanoMF',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -2396.60, 
		y = -2377.98, 
		z = 61.243,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = "Artesano de Thieves Landing",
		id = 'artesanoTL',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -1406.47, 
		y = -2174.47, 
		z = 42.696,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Artesano de Manzanita Post',
		id = 'artesanoMan',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -1986.97,
		y = -1643.14,
		z = 116.128,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Artesano de Owanjila',
		id = 'artesanoOW',
		Job = 0, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -2601.17,
		y = -33.6423,
		z = 160.64,
		Blip = {
			Hash = -1138864184
		},
		Categories = { "Artesano" }
	},
	{
		name = 'Armería de Blackwater',
		id = 'armerobw',
		Job = { "armeriaBW" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
		x = -781.835,
		y = -1325.35,
		z = 43.834,
		Blip = {
			Hash = 0
		},
		Categories = { "Armero" }
	},
    {
		name = 'Armería de Valentine',
		id = 'armeroval',
		Job = { "armeriaVL" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
        x = -281.184,
        y = 777.7536,
        z = 119.55,
		Blip = {
			Hash = 0
		},
		Categories = { "Armero" }
	},
    -- {
	-- 	name = 'Agricultora Taller Oficios',
	-- 	id = 'agriculSDTaller',
	-- 	Job = { "tallerOficios" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = 2057.786,
	-- 	y = -843.252,
	-- 	z = 42.599,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "agricultor" }
	-- },
	-- {
	-- 	name = 'Saloon de Blackwater',
	-- 	id = 'tabernaBW',
	-- 	Job = { "saloonBW" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
    --     x = -819.658,
    --     y = -1319.31,
    --     z = 44.199,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "CocinaTier3", "CocinaTier1", "CocinaTier2", "CocinaMixta", "CocinaPacks" }
	-- },
	-- {
	-- 	name = 'Saloon de Strawberry',
	-- 	id = 'tabernaSW',
	-- 	Job = { "saloonSW" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = -1818.29,
	-- 	y = -434.073,
	-- 	z = 160.43,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "CocinaTier3", "CocinaTier1", "CocinaTier2", "CocinaMixta", "CocinaPacks" }
	-- },
	-- {
	-- 	name = 'Saloon de Valentine',
	-- 	id = 'tabernaVL',
	-- 	Job = { "saloonVL" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = -314.373,
	-- 	y = 810.0457,
	-- 	z = 118.92,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "CocinaTier3", "CocinaTier1", "CocinaTier2", "CocinaMixta", "CocinaPacks" }
	-- },
	-- {
	-- 	name = 'Clinica de Sant Denis',
	-- 	id = 'clinicaSD',
	-- 	Job = { "medicoAR", "medicoBW", "medicoMF" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = 2730.584,
	-- 	y = -1229.12,
	-- 	z = 50.320,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "Medico" }
	-- },
	-- {
	-- 	name = 'Clinica de Rhodes',
	-- 	id = 'clinicaRHO',
	-- 	Job = { "medicoAR", "medicoBW", "medicoMF" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = 1369.673,
	-- 	y = -1305.26,
	-- 	z = 77.921,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "Medico" }
	-- },
	-- {
	-- 	name = 'Clinica de Valentine',
	-- 	id = 'clinicaVL',
	-- 	Job = { "medicoAR", "medicoBW", "medicoMF" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = -282.406,
	-- 	y = 817.8356,
	-- 	z = 119.38,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "Medico" }
	-- },
	-- {
	-- 	name = 'Clinica de Strawberry',
	-- 	id = 'clinicaSW',
	-- 	Job = { "medicoAR", "medicoBW", "medicoMF" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = -1803.21,
	-- 	y = -432.780,
	-- 	z = 158.82,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "Medico" }
	-- },
	-- {
	-- 	name = 'Clinica de Blackwater',
	-- 	id = 'clinicaBW',
	-- 	Job = { "medicoAR", "medicoBW", "medicoMF" }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
	-- 	x = -787.158,
	-- 	y = -1374.94,
	-- 	z = 44.055,
	-- 	Blip = {
	-- 		Hash = 0
	-- 	},
	-- 	Categories = { "Medico" }
	-- },
}

Config.Almacenes = {}

Config.PlaceableCampfire = "p_campfire05x"

-- Restrict campfire usage to specific roles or set to 0 to allow any role
-- Example: { "butcher" }
-- set to 0 to allow any jobs, or like { "butcher" } to job restriction
Config.CampfireJobLock = 0

-- Disables/Enables the kneeling animation when crafting
Config.KneelingAnimation = false

-- Crafting Prop Location is resource intensive, turn this to false if you want to use less resources.
-- Disables/Enables Crafting Props
Config.CraftingPropsEnabled = false

-- Props for the player to craft at
-- List of porps you can use for crafting
-- "P_CAMPFIRECOMBINED01X","p_campfirefresh01x","p_fireplacelogs01x","p_woodstove01x","p_stove04x","p_campfire04x","p_campfire05x","p_campfire02x","p_campfirecombined02x","p_campfirecombined03x","p_kettle03x","p_campfirecombined04x", "P_CAMPFIRECOOK02X","P_CAMPFIRE_WIN2_01X","P_CRAFTINGPOT01X"
Config.CraftingProps = {
}
-- How long the progressbar will show when crafting
Config.CraftTime = 15000

-- Craftable item categories. ident and Config.crafting.Category must equal eachother.
--EXAMPLE:
-- {
--     ident = 'food',
--     text = 'Craft Food',
--     Location = { 'campfire' }, -- set to 0 to allow any locations from Config.Locations
--     Job = { 'butcher' } -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
-- },

-------------------------------------------------------

-- Craftable Items/Rewards And their Recipes
--EXAMPLE:
-- {
--     Text = "Meat Bfast ",
--     SubText = "InvMax = 10",
--     Desc = "Recipe: 1x Meat, 1x Salt",
--     Items = {
--         {
--             name = "meat",
--             count = 1
--         },
--         {
--             name = "salt",
--             count = 1
--         }
--     },
--     Reward = {{
--         {
--             name = "consumable_breakfast", -- if you use the currency mode, you don't need a name section inside the reward section
--             co,}unt = 1
--         }
--     },
--     Job = { 'butcher' }, -- set to 0 to allow any jobs, or like { "butcher" } to job restriction
--     Location = { 'blackwater' }, -- set to 0 to allow any locations from Config.Locations, or like { "butcher" } to job restriction
--     UseCurrencyMode = false, -- true if you want to use the currency mode otherwise set this to false
--     CurrencyType = 0,Location = 0, -- 0 => money, 1 => gold
--     Category = "food",
--     Animation = 'knifecooking' -- set what animation should play when crafting (if this is not set it has a default animation). Animations can be found below in Config.Animations
-- }
Config.Crafting = {
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cebo de pan",
        Desc = "1x Pan, 1x Navaja (↺)",
        Reward = {{name = "p_baitBread01x", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "bread", count = 1, take = true},
            {name = "navaja", count = 1, take = false}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cebo de maíz",
        Desc = "1x Mazorca, 1x Navaja (↺)",
        Reward = {{name = "p_baitCorn01x", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "corn", count = 1, take = true},
            {name = "navaja", count = 1, take = false}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cebo de queso",
        Desc = "1x Cuña de queso, 1x Navaja (↺)",
        Reward = {{name = "p_baitCheese01x", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "consumable_cheese_wedge", count = 1, take = true},
            {name = "navaja", count = 1, take = false}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cigarrillo de Guarma",
        Desc = "1x Papel de liar, 1x Cerilla, 1x Tabaco de Guarma procesado",
        Reward = {{name = "hcigarro", count = 1}},
        Minlvl = 3,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "papel_liar", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "htabaco_proce", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cigarrillo Negro",
        Desc = "1x Papel de liar, 1x Cerilla, 1x Tabaco negro procesado",
        Reward = {{name = "bcigarro", count = 1}},
        Minlvl = 1,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "papel_liar", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "btabaco_proce", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cigarrillo Oriental",
        Desc = "1x Papel de liar, 1x Cerilla, 1x Tabaco oriental procesado",
        Reward = {{name = "ocigarro", count = 1}},
        Minlvl = 2,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "papel_liar", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "otabaco_proce", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cigarrillo Indio",
        Desc = "1x Papel de liar, 1x Cerilla, 1x Tabaco Indio procesado",
        Reward = {{name = "indcigarro", count = 1}},
        Minlvl = 3,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "papel_liar", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "indtobaco_proce", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Cigarrillo Rubio",
        Desc = "1x Papel de liar, 1x Cerilla, 1x Tabaco rubio procesado",
        Reward = {{name = "cigarro", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "papel_liar", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "tabaco_proce", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Flechas",
        Desc = "1x Madera, 1x Hierro, 3x Pluma",
        Reward = {{name = "ammoarrownormal", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "wood", count = 1, take = true},
            {name = "iron", count = 1, take = true},
            {name = "pluma", count = 3, take = true}
        }
    },
	{
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Flechas de punta pequeña",
        Desc = "1x Madera, 1x Hierro, 3x Pluma",
        Reward = {{name = "ammoarrowsmallgame", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "wood", count = 1, take = true},
            {name = "iron", count = 1, take = true},
            {name = "pluma", count = 3, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Hoguera",
        Desc = "8x Palo, 1x Cerilla, 1x Piedra",
        Reward = {{name = "hoguera", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {
            {name = "stick", count = 8, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "piedra", count = 1, take = true}
        }
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Hoguera con Caldero",
        Desc = "1x Hoguera, 1x Olla",
        Reward = {{name = "hoguera_caldero", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "item",
        Items = {{name = "hoguera", count = 1, take = true}, {name = "olla", count = 1, take = true}}
    },
    {
        TakeItems = true,
        CurrencyType = 0,
        Location = 0,
        Animation = "craft",
        Category = "empty",
        Text = "Antorcha",
        Desc = "1x Palo, 1x Cerilla, 2x Trozo de tela",
        Reward = {{name = "WEAPON_MELEE_TORCH", count = 1}},
        Minlvl = 0,
        UseCurrencyMode = false,
        Job = 0,
        Type = "weapon",
        Items = {
            {name = "stick", count = 1, take = true},
            {name = "cerilla", count = 1, take = true},
            {name = "trozotela", count = 2, take = true}
        }
    },
}