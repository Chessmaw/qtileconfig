# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os


mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "w", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "s", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "d", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "a", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "w", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "s", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "d", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "a", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "w", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "s", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "d", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "a", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "k", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),


]



# Test start ● ◕ ◉ ◐ ⚉
__groups = {
    1: Group("",),
    2: Group("𝕏",),
    3: Group("𝕎"),
    4: Group("𝕋"),
    5: Group("𝕄"),
    6: Group("▶"),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ]),
#Test End



#groups = [Group(i) for i in "123456789"]

#for i in groups:
   # keys.extend(
      #  [
            # mod1 + letter of group = switch to group
          #  Key(
          #      [mod],
           #     i.name,
          #      lazy.group[i.name].toscreen(),
          #      desc="Switch to group {}".format(i.name),
          #  ),
            # mod1 + shift + letter of group = switch to & move focused window to group
         #   Key(
       #         [mod, "shift"],
        #        i.name,
        #        lazy.window.togroup(i.name, switch_group=True),
         #       desc="Switch to & move focused window to group {}".format(i.name),
           # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
       # ]
    #)

layouts = [
     layout.MonadTall(
        border_normal="#222222",
        border_focus=None,
        border_width=3,
        single_border_width=0,
        margin=6,
        single_margin=0,
    ),
    layout.Columns(        
        border_normal="#222222",
        border_focus=None,
        border_width=3,
        single_border_width=0,
        margin=10,
        single_margin=0,),
    layout.Max(
        margin=10,
        border_focus=True,
        border_normal="#222222",
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Montserrat",
    fontsize=13,
    padding=8,
    background="#000000",

)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    fontsize=24,
                    highlight_method="line",
                    spacing=0,
                    block_highlight_text_color="#ffffff",
                    borderwidth=0,
                    padding=10
                ),
                
                widget.Prompt(),
                widget.WindowName(foreground="#999999"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#18171c", "#18171c"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                widget.Systray(),
                widget.Clock(background="#000009",format="%a %I:%M %p", foreground="#008080" , fontsize= 16),
                widget.QuickExit( default_text="⏻",fontsize=54,background="#000009"),
                widget.TextBox("Chessmaw",fontsize=16, name="default",background="#100011"),
            ],
            40,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            border_color=["ffffff", "ffffff", "ffffff", "ffffff"],  # Borders are magenta
            margin=10,
            center_aligned=True,
            scroll_repeat=True,
            opacity=0.82,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
autostart = [
        "ulauncher"
        "feh --bg-fill /home/Chessmaw/Pictures/Wallpaper-Chainsaw-Man-Fami",
        "picom --no-vsync &",
        "nm-applet &",
]

for x in autostart:
    os.system(x)