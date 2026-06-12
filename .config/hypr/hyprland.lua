local mainMod = "SUPER"
local terminal = "alacritty"
local fileManager = "nemo"
local menu = "sh /home/silas/.config/desktop/spawn.sh"

-- Environment variables
hl.env("XCURSOR_THEME", "Adwaita")
hl.env("XCURSOR_SIZE", "20")
hl.env("LIBVA_DRIVER_NAME", "nvidia")
hl.env("XDG_SESSION_TYPE", "wayland")
hl.env("GBM_BACKEND", "nvidia-drm")
hl.env("__GLX_VENDOR_LIBRARY_NAME", "nvidia")

hl.config({
	-- unscale XWayland
	xwayland = {
		force_zero_scaling = true,
	},
	cursor = {
		no_hardware_cursors = 1,
	},
	-- Look and feel
	general = {
		gaps_in = 3,
		gaps_out = 0,
		border_size = 2,
		col = {
			active_border = { colors = { "rgba(33ccffee)", "rgba(00ff99ee)" }, angle = 45 },
			inactive_border = "rgba(595959aa)",
		},
		resize_on_border = false,
		allow_tearing = true,
		layout = "dwindle",
	},
	decoration = {
		rounding = 5,
		active_opacity = 1.0,
		inactive_opacity = 1.0,
		shadow = {
			enabled = true,
			range = 4,
			render_power = 3,
			color = "rgba(1a1a1aee)",
		},
		blur = {
			enabled = true,
			size = 3,
			passes = 1,
			vibrancy = 0.1696,
		},
	},
	-- Dwindle layout
	dwindle = {
		preserve_split = true,
	},
	-- Master layout
	master = {
		new_status = "master",
	},
	-- Misc
	misc = {
		disable_hyprland_logo = false,
		focus_on_activate = false,
	},
	-- Input
	input = {
		kb_layout = "de",
		kb_variant = "neo_qwertz",
		follow_mouse = 2,
		float_switch_override_focus = 0,
		sensitivity = 0,
		touchpad = {
			natural_scroll = false,
		},
		tablet = {
			transform = -1,
			output = "current",
			region_position = { 0, 0 },
			absolute_region_position = false,
			region_size = { 0, 0 },
			relative_input = false,
			left_handed = false,
			active_area_size = { 0, 0 },
			active_area_position = { 0, 0 },
		},
	},
})

-- Animations
hl.curve("myBezier", { type = "bezier", points = { { 0.05, 0.9 }, { 0.1, 1.05 } } })
hl.animation({ leaf = "windows", enabled = true, speed = 3, bezier = "myBezier" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = 7, bezier = "default", style = "popin 80%" })
hl.animation({ leaf = "border", enabled = true, speed = 10, bezier = "default" })
hl.animation({ leaf = "borderangle", enabled = true, speed = 8, bezier = "default" })
hl.animation({ leaf = "fade", enabled = true, speed = 3, bezier = "default" })
hl.animation({ leaf = "workspaces", enabled = true, speed = 3, bezier = "default" })

-- Example per-device config
hl.device({
	name = "epic-mouse-v1",
	sensitivity = -0.5,
})

-- Workspaces
hl.workspace_rule({ workspace = "1", default_name = "a", persistent = true, default = true, monitor = "2" })
hl.workspace_rule({ workspace = "2", default_name = "s", persistent = true, default = true, monitor = "1" })
hl.workspace_rule({ workspace = "3", default_name = "d", persistent = true, default = true })
hl.workspace_rule({ workspace = "4", default_name = "f", persistent = true, layout_opts = { orientation = "top" } })
hl.workspace_rule({ workspace = "5", default_name = "g", persistent = true })
hl.workspace_rule({ workspace = "7", default_name = "1", persistent = true, monitor = "0" })
hl.workspace_rule({ workspace = "8", default_name = "2", persistent = true })
hl.workspace_rule({ workspace = "9", default_name = "3", persistent = true })
hl.workspace_rule({ workspace = "10", default_name = "4", persistent = true })
hl.workspace_rule({ workspace = "11", default_name = "5", persistent = true })

-- Window rules
hl.window_rule({ match = { class = "whatsdesk" }, workspace = "4" })
hl.window_rule({ match = { class = "discord" }, workspace = "7" })
hl.window_rule({ match = { class = "^([sS]ignal)$" }, workspace = "4" })
hl.window_rule({ match = { class = "org.mozilla.Thunderbird" }, workspace = "name:g" })
hl.window_rule({ match = { class = ".*.youtube_music" }, workspace = "11" })
hl.window_rule({
	match = {
		class = "thunderbird",
		initial_title = "^(M[^o]|[^M]).*",
	},
	float = true,
})
hl.window_rule({ match = { class = "^(steam.*)$" }, immediate = true })

-- Keybindings
hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd(terminal))
hl.bind(mainMod .. " + B", hl.dsp.exec_cmd("firefox"))
hl.bind(mainMod .. " + W", hl.dsp.window.kill())
hl.bind(
	mainMod .. " + M",
	hl.dsp.exec_cmd(
		'hyprland-dialog --title exit --text "How do you want to exit" --buttons "systemctl suspend;shutdown now;hyprctl dispatch exit" | bash'
	)
)
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(fileManager))
hl.bind(mainMod .. " + T", hl.dsp.window.float())
hl.bind(mainMod .. " + V", hl.dsp.exec_cmd("cliphist list | bemenu | cliphist decode | wl-copy"))
hl.bind(mainMod .. " + R", hl.dsp.exec_cmd(menu))
hl.bind(mainMod .. " + P", hl.dsp.window.pseudo())
hl.bind(mainMod .. " + N", hl.dsp.window.fullscreen())

-- Move focus with mainMod + arrow keys
hl.bind(mainMod .. " + Left", hl.dsp.focus({ direction = "l" }))
hl.bind(mainMod .. " + Right", hl.dsp.focus({ direction = "r" }))
hl.bind(mainMod .. " + Up", hl.dsp.focus({ direction = "u" }))
hl.bind(mainMod .. " + Down", hl.dsp.focus({ direction = "d" }))

-- Move focus with Vim-like keys
hl.bind(mainMod .. " + H", hl.dsp.focus({ direction = "l" }))
hl.bind(mainMod .. " + L", hl.dsp.focus({ direction = "r" }))
hl.bind(mainMod .. " + K", hl.dsp.focus({ direction = "u" }))
hl.bind(mainMod .. " + J", hl.dsp.focus({ direction = "d" }))

-- Resize windows with mainMod + Shift + H/J/K/L
hl.bind(mainMod .. " + SHIFT + H", hl.dsp.window.resize({ x = -100, y = 0, relative = true }))
hl.bind(mainMod .. " + SHIFT + L", hl.dsp.window.resize({ x = 100, y = 0, relative = true }))
hl.bind(mainMod .. " + SHIFT + K", hl.dsp.window.resize({ x = 0, y = -100, relative = true }))
hl.bind(mainMod .. " + SHIFT + J", hl.dsp.window.resize({ x = 0, y = 100, relative = true }))

-- Swap windows with mainMod + Ctrl + Shift + H/J/K/L
hl.bind(mainMod .. " + CTRL + SHIFT + H", hl.dsp.window.swap({ direction = "l" }))
hl.bind(mainMod .. " + CTRL + SHIFT + L", hl.dsp.window.swap({ direction = "r" }))
hl.bind(mainMod .. " + CTRL + SHIFT + K", hl.dsp.window.swap({ direction = "u" }))
hl.bind(mainMod .. " + CTRL + SHIFT + J", hl.dsp.window.swap({ direction = "d" }))

-- Move windows with mainMod + Ctrl + H/J/K/L
hl.bind(mainMod .. " + CTRL + H", hl.dsp.window.move({ direction = "l" }))
hl.bind(mainMod .. " + CTRL + L", hl.dsp.window.move({ direction = "r" }))
hl.bind(mainMod .. " + CTRL + K", hl.dsp.window.move({ direction = "u" }))
hl.bind(mainMod .. " + CTRL + J", hl.dsp.window.move({ direction = "d" }))

-- Switch workspaces with mainMod + [0-9]
hl.bind(mainMod .. " + A", hl.dsp.focus({ workspace = "1", on_current_monitor = true }))
hl.bind(mainMod .. " + S", hl.dsp.focus({ workspace = "2", on_current_monitor = true }))
hl.bind(mainMod .. " + D", hl.dsp.focus({ workspace = "3", on_current_monitor = true }))
hl.bind(mainMod .. " + F", hl.dsp.focus({ workspace = "4", on_current_monitor = true }))
hl.bind(mainMod .. " + G", hl.dsp.focus({ workspace = "5", on_current_monitor = true }))
hl.bind(mainMod .. " + I", hl.dsp.focus({ workspace = "6", on_current_monitor = true }))
hl.bind(mainMod .. " + 1", hl.dsp.focus({ workspace = "7", on_current_monitor = true }))
hl.bind(mainMod .. " + 2", hl.dsp.focus({ workspace = "8", on_current_monitor = true }))
hl.bind(mainMod .. " + 3", hl.dsp.focus({ workspace = "9", on_current_monitor = true }))
hl.bind(mainMod .. " + 4", hl.dsp.focus({ workspace = "10", on_current_monitor = true }))
hl.bind(mainMod .. " + 5", hl.dsp.focus({ workspace = "11", on_current_monitor = true }))

-- Move active window to a workspace with mainMod + Shift + [0-9]
hl.bind(mainMod .. " + SHIFT + A", hl.dsp.window.move({ workspace = "1", follow = false }))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "2", follow = false }))
hl.bind(mainMod .. " + SHIFT + D", hl.dsp.window.move({ workspace = "3", follow = false }))
hl.bind(mainMod .. " + SHIFT + F", hl.dsp.window.move({ workspace = "4", follow = false }))
hl.bind(mainMod .. " + SHIFT + G", hl.dsp.window.move({ workspace = "5", follow = false }))
hl.bind(mainMod .. " + SHIFT + I", hl.dsp.window.move({ workspace = "6", follow = false }))
hl.bind(mainMod .. " + SHIFT + 1", hl.dsp.window.move({ workspace = "7", follow = false }))
hl.bind(mainMod .. " + SHIFT + 2", hl.dsp.window.move({ workspace = "8", follow = false }))
hl.bind(mainMod .. " + SHIFT + 3", hl.dsp.window.move({ workspace = "9", follow = false }))
hl.bind(mainMod .. " + SHIFT + 4", hl.dsp.window.move({ workspace = "10", follow = false }))
hl.bind(mainMod .. " + SHIFT + 5", hl.dsp.window.move({ workspace = "11", follow = false }))

-- Scroll through existing workspaces with mainMod + scroll
hl.bind(mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind(mainMod .. " + mouse_up", hl.dsp.focus({ workspace = "e-1" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- mediabuttons
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("amixer -q sset Master toggle"))
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("amixer -q sset Master 10%-"))
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("amixer -q sset Master 10%+"))
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"))
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"))
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"))
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brillo -q -u 150000 -U 5"))
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brillo -q -u 150000 -A 3"))
hl.bind("XF86Launch7", hl.dsp.exec_cmd("systemctl suspend"))

-- Bind mouse side buttons to tab switching (ctrl + tab / ctrl + shift + tab)
hl.bind("mouse:276", hl.dsp.exec_cmd("ydotool key 29:1 15:1 15:0 29:0"))
hl.bind("mouse:275", hl.dsp.exec_cmd("ydotool key 42:1 29:1 15:1 15:0 29:0 42:0"))

-- Discord keybind passthrough
hl.bind("dead_circumflex", hl.dsp.send_shortcut({ mods = "", key = "dead_circumflex", window = "class:discord" }))
hl.bind("XF86Launch6", hl.dsp.send_shortcut({ mods = "", key = "dead_circumflex", window = "class:discord" }))
hl.bind("ALT + KP_Add", hl.dsp.pass({ window = "class:discord" }))
hl.bind("ALT + KP_Subtract", hl.dsp.pass({ window = "class:discord" }))
hl.bind("ALT + KP_Subtract", hl.dsp.pass({ window = "class:discord" }))

-- hl.bind("dead_circumflex", hl.dsp.send_shortcut({ mods = "", key = "dead_circumflex", window = "title:Event Tester" }))

-- Screenshot submap
hl.bind("ALT + s", hl.dsp.submap("screenshot"))
hl.define_submap("screenshot", function()
	-- WINDOW (w)
	hl.bind(
		"ALT + w",
		hl.dsp.exec_cmd('hyprshot -m window -m active --clipboard-only && notify-send "window captured"')
	)
	hl.bind("ALT + w", hl.dsp.submap("reset"))

	-- MONITOR / OUTPUT (o/m)
	hl.bind(
		"ALT + o",
		hl.dsp.exec_cmd('hyprshot -m output -m active --clipboard-only && notify-send "monitor captured"')
	)
	hl.bind("ALT + o", hl.dsp.submap("reset"))
	hl.bind(
		"ALT + m",
		hl.dsp.exec_cmd('hyprshot -m output -m active --clipboard-only && notify-send "monitor captured"')
	)
	hl.bind("ALT + m", hl.dsp.submap("reset"))

	-- REGION (press ALT+s and release ALT)
	hl.bind(
		"ALT + ALT_L",
		hl.dsp.exec_cmd('hyprshot -m region --clipboard-only && notify-send "region captured"'),
		{ release = true, transparent = true }
	)
	hl.bind("ALT + ALT_L", hl.dsp.submap("reset"), { release = true, transparent = true })

	hl.bind("escape", hl.dsp.submap("reset"))
end)

-- Autostart
hl.on("hyprland.start", function()
	hl.exec_cmd("~/.config/eww/launch_bar")
	hl.exec_cmd("hyprpaper")
	hl.exec_cmd("whatsdesk")
	hl.exec_cmd("ELECTRON_OZONE_PLATFORM_HINT=x11 discord")
	hl.exec_cmd("signal-desktop")
	hl.exec_cmd("thunderbird")
	hl.exec_cmd("pear-desktop")
	hl.exec_cmd("$HOME/.config/desktop/autostart.sh")
	hl.exec_cmd("$HOME/.config/desktop/autostart_wayland.sh")
	-- start hyprland-dummpy.service so graphical-session.target is reached
	hl.exec_cmd("systemctl --user start hyprland-dummy.service")
end)

-- function alert(msg)
--     os.execute(string.format(
--         [[notify-send --app-name=Hyprland --urgency=low --expire-time=1000 "Hyprland Event" "%s"]],
--         msg
--     ))
-- end

-- ---@param monitor HL.Monitor
-- hl.on("monitor.added", function(monitor)
--     alert("Monitor added: " .. table.concat(monitor, ", "))
-- end)
