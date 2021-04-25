from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess

mod = "mod4"            # Sets mod key to SUPER/WINDOWS
terminal = "alacritty"  # My terminal of choice

### KEY BINDINGS
keys = [
    ### WINDOW MANAGEMENT
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Resize windows
    Key([mod, "control"], "p", lazy.layout.maximize(), desc="Toggle a client window between its minimum and maximum sizes"),
    Key([mod, "control"], "o", lazy.layout.normalize(), desc="Reset all secondary client window sizes"),
    Key([mod, "control"], "i", lazy.layout.reset(), desc="Reset all client window sizes"),
    Key([mod, "control"], "j", lazy.layout.grow_main(), desc="Grow main window"),
    Key([mod, "control"], "h", lazy.layout.shrink_main(), desc="Shrink main window"),
    Key([mod, "control"], "l", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "k", lazy.layout.shrink(), desc="Shrink window"),
    
    

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    ### MULTIPLE MONITORS
    Key([mod], "F1", lazy.spawn("/home/alser/.screenlayout/only-external.sh"), lazy.restart(), desc="Only external display"),
    Key([mod], "F2", lazy.spawn("/home/alser/.screenlayout/only-laptop.sh"), lazy.restart(), desc="Only laptop display"),
    Key([mod], "F3", lazy.spawn("/home/alser/.screenlayout/extended-primary-external.sh"), lazy.restart(), desc="Extended vertical layout, external display primary"),
    Key([mod], "F4", lazy.spawn("/home/alser/.screenlayout/extended-primary-laptop.sh"), lazy.restart(), desc="Extended vertical layout, laptop display primary"),

    ### PROGRAMS
    # Rofi 
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Launch Rofi"),  
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show"), desc="Show open program windows in Rofi"),

    # Firefox
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),

    # Chrome
    Key([mod], "c", lazy.spawn("google-chrome-stable"), desc="Launch Chrome"),

    # VS Code
    Key([mod], "v", lazy.spawn("code"), desc="Launch VS Code"),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    ), desc="Volume down"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    ), desc="Volume up"),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    ), desc="Mute audio"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease Brightness"),
]


### COLORS
colors = [["#191919", "#191919"], # 0 - panel background
          ["#3d3f4b", "#434758"], # 1 - background for current screen tab
          ["#ffffff", "#ffffff"], # 2 - font color for group names
          ["#ff5555", "#ff5555"], # 3 - border line color for current tab
          ["#74438f", "#74438f"], # 4 - border line color for 'other tabs' and color for 'odd widgets'
          ["#0167b9", "#0167b9"], # 5 - color for the 'even widgets'
          #["#4f76c7", "#4f76c7"], # 5 - color for the 'even widgets'
          ["#e1acff", "#e1acff"], # 6 - window name
          ["#8e8e8e", "#8e8e8e"]] # 7 - background for inactive screens


### GROUPS
groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups, 1):
    keys.extend([
        ### Switch to selected group
        Key([mod], str(i), lazy.group[group.name].toscreen()),

        ### Send window to selected group
        Key([mod, "shift"], str(i), lazy.window.togroup(group.name))

        ### Or, send window to selected group and switch to that group (uncomment only one)
        # Key([mod, "shift"], i, lazy.window.togroup(group.name, switch_group=True))
    ])



### LAYOUTS
layout_conf = {
    'border_focus': colors[5][0],
    'border_width': 1,
    'margin': 6,
    'min_ratio': 0.5,
    'max_ratio': 0.7,
    'grow_ratio': 0.1
}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f', ),
    layout.Max(**layout_conf),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



### WIDGETS
widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=18,
    padding=3,
    background=colors[0],
    foreground=colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [                      
                widget.GroupBox(
                    font = "UbuntuMono Nerd Font",
                    fontsize = 21,
                    margin_y = 2,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 8,
                    borderwidth = 3,
                    active = colors[2],
                    inactive = colors[7],
                    block_highlight_text_color=colors[2],
                    rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = colors[5],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[6],
                    other_screen_border = colors[4],                       
                ), 
                widget.Prompt(),
                widget.Sep(
                    linewidth = 1,
                    size_percent=70,
                    padding = 20,                       
                ),                
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),   
                widget.TextBox(
                    font = "UbuntuMono Nerd Font",
                    text = '  ',   
                    padding = 4,                                  
                    fontsize = 20,
                ),        
                widget.Net(
                    interface = "wlp1s0"
                ),                       
                widget.TextBox(
                    font = "UbuntuMono Nerd Font",
                    text = '  ',   
                    padding = 4,                                  
                    fontsize = 20,
                ),     
                widget.CheckUpdates(
                    update_interval = 1800,
                    distro = "Arch_checkupdates",
                    display_format = "{updates}",   
                    no_update_string = '0',                                                            
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                ),
                widget.CurrentLayoutIcon(
                    scale=0.70
                ),
                widget.CurrentLayout(),
                widget.Sep(                   
                    linewidth=0,
                    padding = 8,                        
                ),
                widget.Systray(),
                widget.Sep(                   
                    linewidth=0,
                    padding = 8,                        
                ),
                widget.TextBox(
                    font = "UbuntuMono Nerd Font",
                    text = '  ',                        
                    background = colors[5],                     
                    fontsize = 20
                ),     
                widget.Clock(                    
                    background = colors[5],
                    format='%d/%m/%Y %a'
                ),        
                widget.TextBox(
                    font = "UbuntuMono Nerd Font",
                    text = '  ',                        
                    background = colors[5],                     
                    fontsize = 22
                ),                     
                widget.Clock(                    
                    background = colors[5],
                    format='%H:%M'
                ),
                widget.Sep(
                    background = colors[5],
                    linewidth = 0,
                    padding = 8,                       
                ),                             
            ],
            30,
            opacity=1.0
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus=colors[5][0])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"