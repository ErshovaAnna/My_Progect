# -*- coding: utf-8 -*-

import os
import sys
import calendar
import datetime
import mysql.connector

sys.path.append(os.path.abspath(__file__).split('demos')[0])

from kivy import platform


if platform in ('linux', 'macosx', 'windows'):
    from kivy.config import Config

    Config.set('graphics', 'width', '200')
    Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.utils import get_hex_from_color
from kivy.graphics import *

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDInputDialog, MDDialog
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, MDList, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarIconListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theme_picker import MDThemePicker
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.card import MDCardPost
from kivymd.toast import toast
from kivymd.filemanager import MDFileManager
from kivymd.progressloader import MDProgressLoader
from kivymd.stackfloatingbuttons import MDStackFloatingButtons
from kivymd.useranimationcard import MDUserAnimationCard
from libs.applibs.swipetodelete import SwipeBehavior

main_widget_kv = """
#:import Clock kivy.clock.Clock
#:import get_hex_from_color kivy.utils.get_hex_from_color
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import images_path kivymd.images_path
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDTextFieldClear kivymd.textfields.MDTextFieldClear
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDRectangleFlatButton kivymd.button.MDRectangleFlatButton
#:import MDRoundFlatButton kivymd.button.MDRoundFlatButton
#:import MDRoundFlatIconButton kivymd.button.MDRoundFlatIconButton
#:import MDRectangleFlatIconButton kivymd.button.MDRectangleFlatIconButton
#:import MDTextButton kivymd.button.MDTextButton
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import MDUpdateSpinner kivymd.updatespinner.MDUpdateSpinner


<List_Task@BoxLayout>
    orientation: "vertical"
    spacing: 5 
    size_hint_y: None
    hight: self.minimum_height
    
    ThreeLineAvatarIconListItem:
        text: "Call Viber Out"
        secondary_text: "ppp"
        
        IconLeftSampleWidget:
            icon: 'phone' 
        IconRightSampleWidget:       
       
<ContentForAnimCard@BoxLayout>:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        Widget:
        MDRoundFlatButton:
            text: "Free call"
        Widget:
        MDRoundFlatButton:
            text: "Free message"
        Widget:

    OneLineIconListItem:
        text: "Video call"
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        secondary_text:
            "[color=%s]Advantageous rates for calls[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        # FIXME: Don't work "secondary_text_color" parameter
        # secondary_text_color: app.theme_cls.primary_color
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        secondary_text:
            "[color=%s]Operator's tariffs apply[/color]" \
            % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'
   

<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: './assets/drawer_logo.png'

    NavigationDrawerSubheader:
        text: "Menu of Examples:"
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Accordion"
        on_release: app.root.ids.scr_mngr.current = 'accordion'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Bottom Navigation"
        on_release: app.root.ids.scr_mngr.current = 'bottom_navigation'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Bottom Sheets"
        on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Buttons"
        on_release: app.root.ids.scr_mngr.current = 'button'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Cards"
        on_release: app.root.ids.scr_mngr.current = 'card'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Dialogs"
        on_release: app.root.ids.scr_mngr.current = 'dialog'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Download File"
        on_release: app.root.ids.scr_mngr.current = 'download file'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Files Manager"
        on_release: app.root.ids.scr_mngr.current = 'files manager'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Grid lists"
        on_release: app.root.ids.scr_mngr.current = 'grid'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Labels"
        on_release: app.root.ids.scr_mngr.current = 'labels'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Lists"
        on_release: app.root.ids.scr_mngr.current = 'list'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Menus"
        on_release: app.root.ids.scr_mngr.current = 'menu'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Pickers"
        on_release: app.root.ids.scr_mngr.current = 'pickers'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Progress & activity"
        on_release: app.root.ids.scr_mngr.current = 'progress'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Progress bars"
        on_release: app.root.ids.scr_mngr.current = 'progressbars'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Selection controls"
        on_release: app.root.ids.scr_mngr.current = 'selectioncontrols'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Sliders"
        on_release: app.root.ids.scr_mngr.current = 'slider'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Stack Floating Buttons"
        on_release: app.root.ids.scr_mngr.current = 'stack buttons'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Snackbars"
        on_release: app.root.ids.scr_mngr.current = 'snackbar'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Tabs"
        on_release: app.root.ids.scr_mngr.current = 'tabs'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Text fields"
        on_release: app.root.ids.scr_mngr.current = 'textfields'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Themes"
        on_release: app.root.ids.scr_mngr.current = 'theming'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Toolbars"
        on_release: app.root.ids.scr_mngr.current = 'toolbar'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "Update Screen Widget"
        on_release: app.root.ids.scr_mngr.current = 'update spinner'
    NavigationDrawerIconButton:
        icon: 'checkbox-blank-circle'
        text: "User Animation Card"
        on_release: app.root.ids.scr_mngr.current = 'user animation card'


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: 'vertical'

        Toolbar:
            id: toolbar
            title: app.show_year(0)
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            elevation: 10
            left_action_items:
                [['format-color-fill', lambda x: app.theme_picker_open()]]
            right_action_items:
                [['lightbulb-outline', lambda x: app.show_example_alert_dialog()]]

        ScreenManager:
            id: scr_mngr

            Screen:
                name: 'main_screen'
                MDBottomNavigation:
                    id: bottom_navigation_demo

                    MDBottomNavigationItem:
                        name: 'octagon'
                        text: "Месяц"
                        icon: "home-outline"
                        on_enter: app.pusto(k)
                        #on_enter: app.add_cards(grid_card_1)
                        
                        BoxLayout:
                            orientation: "vertical"    
                            spacing: '0dp'
                            padding: '0dp'
                     
                            BoxLayout:
                                orientation: "vertical"
                                
                                BoxLayout:
                                    size_hint: (1, .2)
                                    spacing: '0dp'
                                    padding: '0dp'
                                    #on_release: app.month_now()
            
                                    MDIconButton:
                                        icon: 'arrow-left'
                                        halign: 'left'
                                        on_press: app.previous_month()
            
                                    MDLabel:
                                        id: month_label
                                        font_style: 'Display3'
                                        theme_text_color: 'Primary'
                                        text: app.show_calendar()
                                        halign: 'center'
            
                                    MDIconButton:
                                        icon: 'arrow-right'
                                        halign: 'right'
                                        on_press: app.next_month()
            
                                GridLayout:
                                    cols: 7
                                    padding: dp(35), dp(10), dp(15), dp(0)
                                    spacing: dp(4)
                                    height: self.minimum_height
            
                                    MDLabel:
                                        text: 'ПН'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'ВТ'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'СР'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'ЧТ'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'ПТ'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'СБ'
                                        theme_text_color: 'Error'
                                        #halign: 'center'
                                    MDLabel:
                                        text: 'ВС'
                                        theme_text_color: 'Error'
                                    MDTextButton:
                                        id: textButton_1
                                        text: "1"
                                        font_size: dp(25)
                                        canvas: 
                                        on_press: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_1.text,month_label.text)
                                           
                                    MDTextButton:
                                        id: textButton_2
                                        text: "2"
                                        font_size: dp(25)
                                        on_press: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_2.text,month_label.text)
                                            
                                    MDTextButton:
                                        id: textButton_3
                                        text: "3"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_3.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_4
                                        text: "4"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_4.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_5
                                        text: "5"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_5.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_6
                                        text: "6"
                                        font_size: dp(25) 
                                        opposite_colors: True
                                        theme_text_color: 'Error'
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_6.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_7
                                        text: "7"
                                        font_size: dp(25)
                                        opposite_colors: False
                                        theme_text_color: 'Error'
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_7.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_8
                                        text: "8"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_8.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_9
                                        text: "9"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_9.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_10
                                        text: "10"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_10.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_11
                                        text: "11"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_11.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_12
                                        text: "12"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_12.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_13
                                        text: "13"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_13.text,month_label.text) 
                                    MDTextButton:
                                        id: textButton_14
                                        text: "14"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_14.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_15
                                        text: "15"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_15.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_16
                                        text: "16"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_16.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_17
                                        text: "17"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_17.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_18
                                        text: "18"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_18.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_19
                                        text: "19"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_19.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_20
                                        text: "20"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_20.text,month_label.text) 
                                    MDTextButton:
                                        id: textButton_21
                                        text: "21"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_21.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_22
                                        text: "22"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_22.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_23
                                        text: "23"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_23.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_24
                                        text: "24"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_24.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_25
                                        text: "25"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_25.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_26
                                        text: "26"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_26.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_27
                                        text: "27"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_27.text,month_label.text) 
                                    MDTextButton:
                                        id: textButton_28
                                        text: "28"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_28.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_29
                                        text: "29"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_29.text,month_label.text) 
                                    MDTextButton:
                                        id: textButton_30
                                        text: "30"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_30.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_31
                                        text: "31"
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_31.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_32
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_32.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_33
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_33.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_34
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_34.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_35
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_35.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_36
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_36.text,month_label.text)
                                    MDTextButton:
                                        id: textButton_37
                                        text: ''
                                        font_size: dp(25)
                                        on_release: 
                                            app.root.ids.scr_mngr.current = 'job_entry'
                                            app.change_title(textButton_37.text,month_label.text)

                    MDBottomNavigationItem:
                        id: bottom_navigation
                        name: 'banking'
                        text: "Задание"
                        icon: 'calendar-check'
                        on_enter: 
                            app.nnn(k, month_label.text)
                        #on_leave: app.pusto(k)
                                                    
                        ScrollView:
                            id: scroll
                            size_hint: 1, 1
                            do_scroll_x: False

                            BoxLayout:
                                id: k
                                orientation: "vertical"
                                spacing: 5 
                                size_hint_y: None
                                height: self.minimum_height                       

                    MDBottomNavigationItem:
                        name: 'bottom_navigation_desktop_1'
                        text: "Заметки"
                        icon: 'format-annotation-plus'
                        id: bottom_navigation_desktop_1
                        on_enter:
                            app.pusto(k) 
                            app.test_conection()
                            #app.test_insert()
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: dp(48)
                            spacing: 10
                            MDTextField:
                                hint_text: "Hello again"
               
            ###################################################################
            #
            #                         job_entry  
            #
            ###################################################################
            Screen:
                name: 'job_entry'

                BoxLayout:
                    orientation: "vertical"
                    padding: dp(15)

                    BoxLayout:
                        orientation: "vertical"
                        height: self.minimum_height
                        spacing: '10dp'

                        MDTextField:
                            id: name_job   
                            multiline: True
                            hint_text: "Название дела"
                            helper_text: "Придумайте краткое название"
                            helper_text_mode: "on_focus"
                            #max_text_length: 10
                            
                        MDTextField:
                            id: description
                            multiline: True
                            hint_text: "Описание"
                            #helper_text: "Опишите все подробности задания"
                            #helper_text_mode: "on_focus"


                    BoxLayout:
                        orientation: "vertical"
                        spacing: 5                      
                        
                        MDFloatingActionButton:
                            icon: 'alarm-check'
                            opposite_colors: True
                            md_bg_color: app.theme_cls.primary_color
                            on_press: app.show_example_time_picker()

                        BoxLayout:
                            #spacing: 5 
                            halign: 'left' 
                            MDLabel:
                                text: 'Время:'
                                theme_text_color: 'Primary'    
                            MDLabel:
                                id: time_label
                                theme_text_color: 'Primary'
                                #size_hint: None, None
                                size: dp(48)*3, dp(48)
                            
                    BoxLayout:
                        #size_hint: (1, .2)
                        spacing: '10dp'
                        padding: '10dp'
                        height: self.minimum_height

                        MDFloatingActionButton:
                            icon: 'arrow-left'
                            opposite_colors: True
                            elevation_normal: 8
                            #halign: 'right'
                            md_bg_color: app.theme_cls.primary_color
                            on_press:
                                app.proverka()
                                app.root.ids.scr_mngr.current = 'main_screen'
                                app.show_year(3)

                                
                        MDFloatingActionButton:
                            icon: 'check'
                            opposite_colors: True
                            elevation_normal: 8
                            #halign: 'right'
                            md_bg_color: app.theme_cls.primary_color
                            on_press: 
                                app.test_insert(name_job.text, description.text, time_label.text)
                                #app.root.ids.scr_mngr.current = 'main_screen'
                                #app.dialog_windofs()
                                
                            
            ###################################################################
            #
            #                           DAY
            #
            ###################################################################   
            
            Screen:
                name: 'day'
                on_enter: app.day_task(h);
                
                ScrollView:
                    size_hint: 1, 1
                    #do_scroll_x: False
                    BoxLayout:
                        id: h
                        orientation: "vertical"
                        spacing: 5 
                        halign: 'centr' 
                         
                    

                #    MDList:
                #        id: ml
                #        ThreeLineListItem:
                #            id: day_label
                #            #text: "Three-line item"
                #            #secondary_text:
                #                #"This is a multi-line label where you can " \
                #                #"fit more text than usual"
                    
                
            

            ###################################################################
            #
            #                          BOTTOM SHEET
            #
            ###################################################################

            Screen:
                name: 'bottomsheet'

                MDRaisedButton:
                    text: "Open list bottom sheet"
                    opposite_colors: True
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    on_release: app.show_example_bottom_sheet()

                MDRaisedButton:
                    text: "Open grid bottom sheet"
                    opposite_colors: True
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: app.show_example_grid_bottom_sheet()

            ###################################################################
            #
            #                            BUTTONS
            #
            ###################################################################

            Screen:
                name: 'button'

                BoxLayout:
                    size_hint_y: None
                    height: '56'
                    spacing: '10dp'
                    pos_hint: {'center_y': .9}

                    Widget:

                    MDIconButton:
                        icon: 'sd'

                    MDFloatingActionButton:
                        icon: 'plus'
                        opposite_colors: True
                        elevation_normal: 8

                    MDFloatingActionButton:
                        icon: 'check'
                        opposite_colors: True
                        elevation_normal: 8
                        md_bg_color: app.theme_cls.primary_color

                    MDIconButton:
                        icon: 'sd'
                        theme_text_color: 'Custom'
                        text_color: app.theme_cls.primary_color

                    Widget:

                MDFlatButton:
                    text: 'MDFlatButton'
                    pos_hint: {'center_x': 0.5, 'center_y': .75}

                MDRaisedButton:
                    text: "MDRaisedButton"
                    elevation_normal: 2
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': .65}

                MDRectangleFlatButton:
                    text: "MDRectangleFlatButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .55}

                MDRectangleFlatIconButton:
                    text: "MDRectangleFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': 0.5, 'center_y': .45}
                    width: dp(230)

                MDRoundFlatButton:
                    text: "MDRoundFlatButton"
                    icon: "language-python"
                    pos_hint: {'center_x': 0.5, 'center_y': .35}

                MDRoundFlatIconButton:
                    text: "MDRoundFlatIconButton"
                    icon: "language-python"
                    pos_hint: {'center_x': 0.5, 'center_y': .25}
                    width: dp(200)

                MDFillRoundFlatButton:
                    text: "MDFillRoundFlatButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .15}

                MDTextButton:
                    text: "MDTextButton"
                    pos_hint: {'center_x': 0.5, 'center_y': .05}

            ###################################################################
            #
            #                            CARDS
            #
            ###################################################################

            Screen:
                name: 'card'
                on_enter: app.add_cards(grid_card)

                ScrollView:
                    id: scroll
                    size_hint: 1, 1
                    do_scroll_x: False

                    GridLayout:
                        id: grid_card
                        cols: 1
                        spacing: dp(5)
                        padding: dp(5)
                        size_hint_y: None
                        height: self.minimum_height

                        # See how to add a card with the menu and others
                        # in the add_cards function.

            ###################################################################
            #
            #                        DOWNLOAD FILE
            #
            ###################################################################

            Screen:
                name: 'download file'

                FloatLayout:
                    id: box_flt

                    MDRaisedButton:
                        text: "Download file"
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        opposite_colors: True
                        on_release:
                            Clock.schedule_once(\
                            app.show_example_download_file, .1)

            ###################################################################
            #
            #                            DIALOGS
            #
            ###################################################################

            Screen:
                name: 'dialog'

                MDRaisedButton:
                    text: "Open lengthy dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                    opposite_colors: True
                    on_release: app.show_example_long_dialog()

                MDRaisedButton:
                    text: "Open input dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    opposite_colors: True
                    on_release: app.show_example_input_dialog()

                MDRaisedButton:
                    text: "Open Alert Dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    opposite_colors: True
                    on_release: app.show_example_alert_dialog()

                MDRaisedButton:
                    text: "Open Ok Cancel Dialog"
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    opposite_colors: True
                    on_release: app.show_example_ok_cancel_dialog()

            ###################################################################
            #
            #                             GRID
            #
            ###################################################################

            Screen:
                name: 'grid'

                ScrollView:
                    do_scroll_x: False

                    GridLayout:
                        cols: 3
                        row_default_height:
                            (self.width - self.cols*self.spacing[0])/self.cols
                        row_force_default: True
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(4), dp(4)
                        spacing: dp(4)

                        SmartTileWithLabel:
                            mipmap: True
                            source: './assets/african-lion-951778_1280.jpg'
                            text: "African Lion"
                        SmartTile:
                            mipmap: True
                            source: './assets/beautiful-931152_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/african-lion-951778_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/guitar-1139397_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/robin-944887_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/kitten-1049129_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/light-bulb-1042480_1280.jpg'
                        SmartTile:
                            mipmap: True
                            source: './assets/tangerines-1111529_1280.jpg'

            ###################################################################
            #
            #                             LABELS
            #
            ###################################################################

            Screen:
                name: 'labels'

                ScrollView:
                    do_scroll_x: False

                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(1000)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Body1 label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body2'
                                theme_text_color: 'Primary'
                                text: "Body2 label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Caption'
                                theme_text_color: 'Primary'
                                text: "Caption label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Subhead'
                                theme_text_color: 'Primary'
                                text: "Subhead label"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Title'
                                theme_text_color: 'Primary'
                                text: "Title label"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Headline'
                                theme_text_color: 'Primary'
                                text: "Headline label"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Display1'
                            theme_text_color: 'Primary'
                            text: "Display1 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display2'
                            theme_text_color: 'Primary'
                            text: "Display2 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display3'
                            theme_text_color: 'Primary'
                            text: "Display3 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        MDLabel:
                            font_style: 'Display4'
                            theme_text_color: 'Primary'
                            text: "Display4 label"
                            halign: 'center'
                            size_hint_y: None
                            height: self.texture_size[1] + dp(4)
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Primary'
                                text: "Primary color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Secondary'
                                text: "Secondary color"
                                halign: 'center'
                        BoxLayout:
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Hint'
                                text: "Hint color"
                                halign: 'center'
                            MDLabel:
                                font_style: 'Body1'
                                theme_text_color: 'Error'
                                text: "Error color"
                                halign: 'center'
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Custom'
                            text_color: (0,1,0,.4)
                            text: "Custom"
                            halign: 'center'

            ###################################################################
            #
            #                             LISTS
            #
            ###################################################################

            Screen:
                name: 'list'

                ScrollView:
                    do_scroll_x: False

                    MDList:
                        id: ml
                        OneLineListItem:
                            text: "One-line item"
                        TwoLineListItem:
                            text: "Two-line item"
                            secondary_text: "Secondary text here"
                        ThreeLineListItem:
                            text: "Three-line item"
                            secondary_text:
                                "This is a multi-line label where you can " \
                                "fit more text than usual"
                        OneLineAvatarListItem:
                            text: "Single-line item with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        TwoLineAvatarListItem:
                            type: "two-line"
                            text: "Two-line item..."
                            secondary_text: "with avatar"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        ThreeLineAvatarListItem:
                            type: "three-line"
                            text: "Three-line item..."
                            secondary_text:
                                "...with avatar..." + '\\n' + "and third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                        OneLineIconListItem:
                            text: "Single-line item with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_1
                                icon: 'star-circle'
                        TwoLineIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with left icon"
                            IconLeftSampleWidget:
                                id: li_icon_2
                                icon: 'comment-text'
                        ThreeLineIconListItem:
                            text: "Three-line item..."
                            secondary_text:
                                "...with left icon..." + '\\n' + "and " \
                                "third line!"
                            IconLeftSampleWidget:
                                id: li_icon_3
                                icon: 'sd'
                        OneLineAvatarIconListItem:
                            text: "Single-line + avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        TwoLineAvatarIconListItem:
                            text: "Two-line item..."
                            secondary_text: "...with avatar&icon"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:
                        ThreeLineAvatarIconListItem:
                            text: "Three-line item..."
                            secondary_text:
                                "...with avatar&icon..." + '\\n' + "and " \
                                "third line!"
                            AvatarSampleWidget:
                                source: './assets/avatar.png'
                            IconRightSampleWidget:

            ###################################################################
            #
            #                         FILES MANAGER
            #
            #       See the help on using the file in the file filemanager.py
            #
            ###################################################################

            Screen:
                name: 'files manager'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open files manager'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.file_manager_open()

            ###################################################################
            #
            #                             MENUS
            #
            ###################################################################

            Screen:
                name: 'menu'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.2, 'center_y': 0.9}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.2, 'center_y': 0.1}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.8, 'center_y': 0.1}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.8, 'center_y': 0.9}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=3).open(self)

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open menu'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release:
                        MDDropdownMenu(\
                        items=app.menu_items, width_mult=4).open(self)

            ###################################################################
            #
            #                             CHECKBOX
            #
            ###################################################################

            Screen:
                name: 'progress'

                MDCheckbox:
                    id: chkbox
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    active: True
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    active: True if chkbox.active else False

            ###################################################################
            #
            #                          PROGRESS BAR
            #
            ###################################################################

            Screen:
                name: 'progressbars'

                BoxLayout:
                    orientation:'vertical'
                    padding: '8dp'

                    MDSlider:
                        id:progress_slider
                        min:0
                        max:100
                        value: 40

                    MDProgressBar:
                        value: progress_slider.value
                    MDProgressBar:
                        reversed: True
                        value: progress_slider.value

                    BoxLayout:
                        MDProgressBar:
                            orientation:"vertical"
                            reversed: True
                            value: progress_slider.value

                        MDProgressBar:
                            orientation:"vertical"
                            value: progress_slider.value

            ###################################################################
            #
            #                         UPDATE SPINNER
            #
            ###################################################################

            Screen:
                name: 'update spinner'
                on_enter: upd_lbl.text = "Pull to string update"
                on_leave: upd_lbl.text = ""

                MDLabel:
                    id: upd_lbl
                    font_style: 'Display2'
                    theme_text_color: 'Primary'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    size_hint_y: None
                    height: self.texture_size[1] + dp(4)

                MDUpdateSpinner:
                    event_update: lambda x: app.update_screen(self)

            ###################################################################
            #
            #                     STACK FLOATING BUTTONS
            #
            ###################################################################

            Screen:
                name: 'stack buttons'
                on_enter: app.example_add_stack_floating_buttons()

            ###################################################################
            #
            #                          SLIDER
            #
            ###################################################################

            Screen:
                name: 'slider'

                BoxLayout:
                    MDSlider:
                        id: hslider
                        min:0
                        max:100
                        value: 10
                    MDSlider:
                        id: vslider
                        orientation:'vertical'
                        min:0
                        max:100
                        value: hslider.value

            ###################################################################
            #
            #                      USER ANIMATION CARD
            #
            ###################################################################

            Screen:
                name: 'user animation card'

                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open card'
                    opposite_colors: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    on_release: app.show_user_example_animation_card()

            ###################################################################
            #
            #                      SELECTION CONTROLS
            #
            ###################################################################

            Screen:
                name: 'selectioncontrols'

                MDCheckbox:
                    id: grp_chkbox_1
                    group: 'test'
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.25, 'center_y': 0.5}
                MDCheckbox:
                    id: grp_chkbox_2
                    group: 'test'
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDSwitch:
                    size_hint: None, None
                    size: dp(36), dp(48)
                    pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                    _active: False

            ###################################################################
            #
            #                           SNACKBAR
            #
            ###################################################################

            Screen:
                name: 'snackbar'

                MDRaisedButton:
                    text: "Create simple snackbar"
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('simple')
                MDRaisedButton:
                    text: "Create snackbar with button"
                    size_hint: None, None
                    size: 4 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('button')
                MDRaisedButton:
                    text: "Create snackbar with a lot of text"
                    size_hint: None, None
                    size: 5 * dp(48), dp(48)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                    opposite_colors: True
                    on_release: app.show_example_snackbar('verylong')

            ###################################################################
            #
            #                         TEXTFIELDS
            #
            ###################################################################

            Screen:
                name: 'textfields'

                ScrollView:

                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: dp(48)
                        spacing: 10

                        MDTextField:
                            hint_text: "No helper text"
                        MDTextField:
                            hint_text: "Helper text on focus"
                            helper_text:
                                "This will disappear when you click off"
                            helper_text_mode: "on_focus"
                        MDTextField:
                            hint_text: "Persistent helper text"
                            helper_text: "Text is always here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            id: text_field_error
                            hint_text:
                                "Helper text on error (Hit Enter with " \
                                "two characters here)"
                            helper_text: "Two is my least favorite number"
                            helper_text_mode: "on_error"
                        MDTextField:
                            hint_text: "Max text length = 10"
                            max_text_length: 10
                        MDTextField:
                            hint_text: "required = True"
                            required: True
                            helper_text_mode: "on_error"
                        MDTextField:
                            multiline: True
                            hint_text: "Multi-line text"
                            helper_text: "Messages are also supported here"
                            helper_text_mode: "persistent"
                        MDTextField:
                            hint_text: "color_mode = \'accent\'"
                            color_mode: 'accent'
                        MDTextField:
                            hint_text: "color_mode = \'custom\'"
                            color_mode: 'custom'
                            helper_text_mode: "on_focus"
                            helper_text:
                                "Color is defined by \'line_color_focus\' " \
                                "property"
                            line_color_focus:
                                # This is the color used by the textfield
                                self.theme_cls.opposite_bg_normal
                        MDTextField:
                            hint_text: "disabled = True"
                            disabled: True
                        MDTextFieldClear:
                            hint_text: "Text field with clearing type"

            ###################################################################
            #
            #                          THEMING
            #
            ###################################################################

            Screen:
                name: 'theming'

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: dp(80)
                    center_y: self.parent.center_y

                    MDRaisedButton:
                        size_hint: None, None
                        size: 3 * dp(48), dp(48)
                        center_x: self.parent.center_x
                        text: 'Change theme'
                        on_release: app.theme_picker_open()
                        opposite_colors: True
                        pos_hint: {'center_x': 0.5}
                    MDLabel:
                        text:
                            "Current: " + app.theme_cls.theme_style + \
                            ", " + app.theme_cls.primary_palette
                        theme_text_color: 'Primary'
                        pos_hint: {'center_x': 0.5}
                        halign: 'center'

            ###################################################################
            #
            #                         TOOLBARS
            #
            ###################################################################

            Screen:
                name: 'toolbar'

                Toolbar:
                    title: "Simple toolbar"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                    md_bg_color: get_color_from_hex(colors['Teal']['500'])
                    background_palette: 'Teal'
                    background_hue: '500'
                Toolbar:
                    title: "Toolbar with right buttons"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: get_color_from_hex(colors['Amber']['700'])
                    background_palette: 'Amber'
                    background_hue: '700'
                    right_action_items: [['content-copy', lambda x: None]]
                Toolbar:
                    title: "Toolbar with left and right buttons"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                    md_bg_color: get_color_from_hex(colors['DeepPurple']['A400'])
                    background_palette: 'DeepPurple'
                    background_hue: 'A400'
                    left_action_items: [['arrow-left', lambda x: None]]
                    right_action_items: [['lock', lambda x: None], \
                        ['camera', lambda x: None], \
                        ['play', lambda x: None]]

            ###################################################################
            #
            #                              TABS
            #
            ###################################################################

            Screen:
                name: 'tabs'

                MDTabbedPanel:
                    id: tab_panel
                    tab_display_mode:'text'

                    MDTab:
                        name: 'music'
                        text: "Music" # Why are these not set!!!
                        icon: "playlist-play"
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Here is my music list :)"
                            halign: 'center'
                    MDTab:
                        name: 'movies'
                        text: 'Movies'
                        icon: "movie"

                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Show movies here :)"
                            halign: 'center'

                BoxLayout:
                    size_hint_y:None
                    height: '48dp'
                    padding: '12dp'

                    MDLabel:
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                        text: "Use icons"
                        size_hint_x:None
                        width: '64dp'
                    MDCheckbox:
                        on_state: tab_panel.tab_display_mode = 'icons' if tab_panel.tab_display_mode=='text' else 'text'

            ###################################################################
            #
            #                            ACCORDION
            #
            ###################################################################

            Screen:
                name: 'accordion'

                BoxLayout:

                    MDAccordion:
                        orientation: 'vertical'
                        size_hint_x: None
                        width: '240dp'

                        MDAccordionItem:
                            title:'Item 1'
                            icon: 'home'
                            MDAccordionSubItem:
                                text: "Subitem 1"
                            MDAccordionSubItem:
                                text: "Subitem 2"
                            MDAccordionSubItem:
                                text: "Subitem 3"
                        MDAccordionItem:
                            title:'Item 2'
                            icon: 'earth'
                            MDAccordionSubItem:
                                text: "Subitem 4"
                            MDAccordionSubItem:
                                text: "Subitem 5"
                            MDAccordionSubItem:
                                text: "Subitem 6"
                        MDAccordionItem:
                            title:'Item 3'
                            icon: 'account'
                            MDAccordionSubItem:
                                text: "Subitem 7"
                            MDAccordionSubItem:
                                text: "Subitem 8"
                            MDAccordionSubItem:
                                text: "Subitem 9"

                    MDLabel:
                        text: 'Content'
                        theme_text_color: 'Primary'

            ###################################################################
            #
            #                           PICKERS
            #
            ###################################################################

            Screen:
                name: 'pickers'

                BoxLayout:
                    spacing: dp(40)
                    orientation: 'vertical'
                    size_hint_x: None
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    BoxLayout:
                        orientation: 'vertical'
                        # size_hint: (None, None)

                        MDRaisedButton:
                            text: "Open time picker"
                            size_hint: None, None
                            size: 3 * dp(48), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            opposite_colors: True
                            on_release: app.show_example_time_picker()
                        MDLabel:
                            id: time_picker_label
                            theme_text_color: 'Primary'
                            size_hint: None, None
                            size: dp(48)*3, dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        BoxLayout:
                            size: dp(48)*3, dp(48)
                            size_hint: (None, None)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            MDLabel:
                                theme_text_color: 'Primary'
                                text: "Start on previous time"
                                size_hint: None, None
                                size: dp(130), dp(48)
                            MDCheckbox:
                                id: time_picker_use_previous_time
                                size_hint: None, None
                                size: dp(48), dp(48)

                    BoxLayout:
                        orientation: 'vertical'

                        MDRaisedButton:
                            text: "Open date picker"
                            size_hint: None, None
                            size: 3 * dp(48), dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            opposite_colors: True
                            on_release: app.show_example_date_picker()
                        MDLabel:
                            id: date_picker_label
                            theme_text_color: 'Primary'
                            size_hint: None, None
                            size: dp(48)*3, dp(48)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        BoxLayout:
                            size: dp(48)*3, dp(48)
                            size_hint: (None, None)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            MDLabel:
                                theme_text_color: 'Primary'
                                text: "Start on previous date"
                                size_hint: None, None
                                size: dp(130), dp(48)
                            MDCheckbox:
                                id: date_picker_use_previous_date
                                size_hint: None, None
                                size: dp(48), dp(48)

            ###################################################################
            #
            #                       BOTTOM NAVIGATION
            #
            ###################################################################

            Screen:
                name: 'bottom_navigation'

                MDBottomNavigation:
                    id: bottom_navigation_demo

                    MDBottomNavigationItem:
                        name: 'octagon'
                        text: "Warning"
                        icon: "alert-octagon"
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Warning!"
                            halign: 'center'

                    MDBottomNavigationItem:
                        name: 'banking'
                        text: "Bank"
                        icon: 'bank'
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: dp(48)
                            spacing: 10
                            MDTextField:
                                hint_text: "You can put any widgets here"
                                helper_text: "Hello :)"
                                helper_text_mode: "on_focus"

                    MDBottomNavigationItem:
                        name: 'bottom_navigation_desktop_1'
                        text: "Hello"
                        icon: 'alert'
                        id: bottom_navigation_desktop_1
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: dp(48)
                            spacing: 10
                            MDTextField:
                                hint_text: "Hello again"

                    MDBottomNavigationItem:
                        name: 'bottom_navigation_desktop_2'
                        text: "Food"
                        icon: 'food'
                        id: bottom_navigation_desktop_2
                        MDLabel:
                            font_style: 'Body1'
                            theme_text_color: 'Primary'
                            text: "Cheese!"
                            halign: 'center'
"""


class KitchenSink(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'
    previous_date = ObjectProperty()

    def __init__(self, **kwargs):
        super(KitchenSink, self).__init__(**kwargs)

        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="A28nn09a",
            database = 'new_schema',
            auth_plugin='mysql_native_password'
        )

        self.menu_items = [
            {'viewclass': 'MDMenuItem',
             'text': 'Example item %d' % i,
             'callback': self.callback_for_menu_items}
            for i in range(15)
        ]
        self.left_action=[
            {
                'icon' : 'sd'
            }
        ]
        self.Window = Window
        self.manager = False
        self.md_theme_picker = None
        self.long_dialog = None
        self.input_dialog = None
        self.alert_dialog = None
        self.alert_dialog1 = None
        self.alert_dialog2 = None
        self.ok_cancel_dialog = None
        self.long_dialog = None
        self.dialog = None
        self.user_animation_card = None
        self.manager_open = False
        self.cards_created = False
        self.file_manager = None
        self.bs_menu_1 = None
        self.bs_menu_2 = None
        self.tick = 0
        self.create_stack_floating_buttons = False
        self.month_calendar = None
        self.name_year = None
        self.name_name = None
        self.name_discription = None
        self.lenwidget = 0
        self.num_month = 0
        self.datetim = ''
        Window.bind(on_keyboard=self.events)
        self.mycursor = self.mydb.cursor()

    def test_conection(self):

        #self.mycursor = self.mydb.cursor()
        task = []
        #self.mycursor.execute("SELECT * FROM new_table")
        self.mycursor.execute("SELECT name FROM new_schema.new_table;")
        for x in self.mycursor:
            task.append(x)
        print(task)


    def get_string1(self, string1, string2):
        print(string1)
        print(string2)
        self.name_name = str(string1)
        self.name_discription = str(string2)
        #self.main_widget.ids.day_label.text = str(string1)
        #self.main_widget.ids.day_label.secondary_text = str(string2)

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_label.text = str(time)
        self.previous_time = time
    def show_calendar(self):

        mydate = datetime.datetime.now()
        self.name_year = datetime.datetime.now().year

        if mydate.strftime("%B") == 'January':
            self.name_month = 'Январь'
            return self.name_month
        elif mydate.strftime("%B") == 'Febuary':
            self.name_month = 'Февраль'
            return self.name_month
        elif mydate.strftime("%B") == 'March':
            self.name_month = 'Март'
            return self.name_month
        elif mydate.strftime("%B") == 'April':
            self.name_month = 'Апрель'
            return self.name_month
        elif mydate.strftime("%B") == 'May':
            self.name_month = 'Май'
            return self.name_month
        elif mydate.strftime("%B") == 'June':
            self.name_month = 'Июнь'
            return self.name_month
        elif mydate.strftime("%B") == 'July':
            self.name_month = 'Июль'
            return self.name_month
        elif mydate.strftime("%B") == 'August':
            self.name_month = 'Август'
            return self.name_month
        elif mydate.strftime("%B") == 'September':
            self.name_month = 'Сентябрь'
            return self.name_month
        elif mydate.strftime("%B") == 'October':
            self.name_month = 'Октябрь'
            return self.name_month
        elif mydate.strftime("%B") == 'November':
            self.name_month = 'Ноябрь'
            return self.name_month
        elif mydate.strftime("%B") == 'December':
            self.name_month = 'Декабрь'
            return self.name_month


    def test_insert(self, name, discription, time):
        if (self.main_widget.ids.name_job.text != '') or (self.main_widget.ids.time_label.text != ''):
            self.datetim = self.datetim + ' ' + str(time)
            print(self.datetim)
            sql = "INSERT INTO new_table(name, description, date_time) VALUES(%s, %s, %s)"
            val = (name, discription, str(self.datetim))
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            self.main_widget.ids.name_job.text = ''
            self.main_widget.ids.time_label.text = ''
            self.main_widget.ids.description.text = ''
            self.main_widget.ids.scr_mngr.get_screen('main_screen')

            self.dialog_windofs()
        else:
            self.dialog_exeption()

    def show_year(self, s):

        if s == 0:
            return str(self.name_year)
        if s == 1:
            self.name_year = self.name_year + 1
            return str(self.name_year)
        if s == 2:
            self.name_year = self.name_year - 1
            return str(self.name_year)
        if s == 3:
            self.main_widget.ids.toolbar.title = str(self.name_year)

    def proverka(self):
        print(self.main_widget.ids.time_label.text)

    def number_day(self, day_start, day_finish):
        if day_start == 0:
            self.main_widget.ids.textButton_1.text = '1'
            self.main_widget.ids.textButton_2.text = '2'
            self.main_widget.ids.textButton_3.text = '3'
            self.main_widget.ids.textButton_4.text = '4'
            self.main_widget.ids.textButton_5.text = '5'
            self.main_widget.ids.textButton_6.text = '6'
            self.main_widget.ids.textButton_7.text = '7'
            self.main_widget.ids.textButton_8.text = '8'
            self.main_widget.ids.textButton_9.text = '9'
            self.main_widget.ids.textButton_10.text = '10'
            self.main_widget.ids.textButton_11.text = '11'
            self.main_widget.ids.textButton_12.text = '12'
            self.main_widget.ids.textButton_13.text = '13'
            self.main_widget.ids.textButton_14.text = '14'
            self.main_widget.ids.textButton_15.text = '15'
            self.main_widget.ids.textButton_16.text = '16'
            self.main_widget.ids.textButton_17.text = '17'
            self.main_widget.ids.textButton_18.text = '18'
            self.main_widget.ids.textButton_19.text = '19'
            self.main_widget.ids.textButton_20.text = '20'
            self.main_widget.ids.textButton_21.text = '21'
            self.main_widget.ids.textButton_22.text = '22'
            self.main_widget.ids.textButton_23.text = '23'
            self.main_widget.ids.textButton_24.text = '24'
            self.main_widget.ids.textButton_25.text = '25'
            self.main_widget.ids.textButton_26.text = '26'
            self.main_widget.ids.textButton_27.text = '27'
            self.main_widget.ids.textButton_28.text = '28'

            if day_finish == 28:

                self.main_widget.ids.textButton_29.text = ''
                self.main_widget.ids.textButton_30.text = ''
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            elif day_finish == 29:

                self.main_widget.ids.textButton_29.text = '29'
                self.main_widget.ids.textButton_30.text = ''
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

            elif day_finish == 30:

                self.main_widget.ids.textButton_29.text = '29'
                self.main_widget.ids.textButton_30.text = '30'
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            elif day_finish == 31:

                self.main_widget.ids.textButton_29.text = '29'
                self.main_widget.ids.textButton_30.text = '30'
                self.main_widget.ids.textButton_31.text = '31'
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

        elif day_start == 1:
            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = '1'
            self.main_widget.ids.textButton_3.text = '2'
            self.main_widget.ids.textButton_4.text = '3'
            self.main_widget.ids.textButton_5.text = '4'
            self.main_widget.ids.textButton_6.text = '5'
            self.main_widget.ids.textButton_7.text = '6'
            self.main_widget.ids.textButton_8.text = '7'
            self.main_widget.ids.textButton_9.text = '8'
            self.main_widget.ids.textButton_10.text = '9'
            self.main_widget.ids.textButton_11.text = "10"
            self.main_widget.ids.textButton_12.text = '11'
            self.main_widget.ids.textButton_13.text = '12'
            self.main_widget.ids.textButton_14.text = '13'
            self.main_widget.ids.textButton_15.text = '14'
            self.main_widget.ids.textButton_16.text = '15'
            self.main_widget.ids.textButton_17.text = '16'
            self.main_widget.ids.textButton_18.text = '17'
            self.main_widget.ids.textButton_19.text = '18'
            self.main_widget.ids.textButton_20.text = '19'
            self.main_widget.ids.textButton_21.text = '20'
            self.main_widget.ids.textButton_22.text = '21'
            self.main_widget.ids.textButton_23.text = '22'
            self.main_widget.ids.textButton_24.text = '23'
            self.main_widget.ids.textButton_25.text = '24'
            self.main_widget.ids.textButton_26.text = '25'
            self.main_widget.ids.textButton_27.text = '26'
            self.main_widget.ids.textButton_28.text = '27'
            self.main_widget.ids.textButton_29.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_30.text = ''
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 29:
                self.main_widget.ids.textButton_30.text = '29'
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 30:
                self.main_widget.ids.textButton_30.text = '29'
                self.main_widget.ids.textButton_31.text = '30'
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 31:
                self.main_widget.ids.textButton_30.text = '29'
                self.main_widget.ids.textButton_31.text = '30'
                self.main_widget.ids.textButton_32.text = '31'
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

        elif day_start == 2:

            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = ''
            self.main_widget.ids.textButton_3.text = '1'
            self.main_widget.ids.textButton_4.text = '2'
            self.main_widget.ids.textButton_5.text = '3'
            self.main_widget.ids.textButton_6.text = '4'
            self.main_widget.ids.textButton_7.text = '5'
            self.main_widget.ids.textButton_8.text = '6'
            self.main_widget.ids.textButton_9.text = '7'
            self.main_widget.ids.textButton_10.text = '8'
            self.main_widget.ids.textButton_11.text = "9"
            self.main_widget.ids.textButton_12.text = '10'
            self.main_widget.ids.textButton_13.text = '11'
            self.main_widget.ids.textButton_14.text = '12'
            self.main_widget.ids.textButton_15.text = '13'
            self.main_widget.ids.textButton_16.text = '14'
            self.main_widget.ids.textButton_17.text = '15'
            self.main_widget.ids.textButton_18.text = '16'
            self.main_widget.ids.textButton_19.text = '17'
            self.main_widget.ids.textButton_20.text = '18'
            self.main_widget.ids.textButton_21.text = '19'
            self.main_widget.ids.textButton_22.text = '20'
            self.main_widget.ids.textButton_23.text = '21'
            self.main_widget.ids.textButton_24.text = '22'
            self.main_widget.ids.textButton_25.text = '23'
            self.main_widget.ids.textButton_26.text = '24'
            self.main_widget.ids.textButton_27.text = '25'
            self.main_widget.ids.textButton_28.text = '26'
            self.main_widget.ids.textButton_29.text = '27'
            self.main_widget.ids.textButton_30.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_31.text = ''
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 29:
                self.main_widget.ids.textButton_31.text = '29'
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 30:
                self.main_widget.ids.textButton_31.text = '29'
                self.main_widget.ids.textButton_32.text = '30'
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 31:
                self.main_widget.ids.textButton_31.text = '29'
                self.main_widget.ids.textButton_32.text = '30'
                self.main_widget.ids.textButton_33.text = '31'
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
        if day_start == 3:
            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = ''
            self.main_widget.ids.textButton_3.text = ''
            self.main_widget.ids.textButton_4.text = '1'
            self.main_widget.ids.textButton_5.text = '2'
            self.main_widget.ids.textButton_6.text = '3'
            self.main_widget.ids.textButton_7.text = '4'
            self.main_widget.ids.textButton_8.text = '5'
            self.main_widget.ids.textButton_9.text = '6'
            self.main_widget.ids.textButton_10.text = '7'
            self.main_widget.ids.textButton_11.text = "8"
            self.main_widget.ids.textButton_12.text = '9'
            self.main_widget.ids.textButton_13.text = '10'
            self.main_widget.ids.textButton_14.text = '11'
            self.main_widget.ids.textButton_15.text = '12'
            self.main_widget.ids.textButton_16.text = '13'
            self.main_widget.ids.textButton_17.text = '14'
            self.main_widget.ids.textButton_18.text = '15'
            self.main_widget.ids.textButton_19.text = '16'
            self.main_widget.ids.textButton_20.text = '17'
            self.main_widget.ids.textButton_21.text = '18'
            self.main_widget.ids.textButton_22.text = '19'
            self.main_widget.ids.textButton_23.text = '20'
            self.main_widget.ids.textButton_24.text = '21'
            self.main_widget.ids.textButton_25.text = '22'
            self.main_widget.ids.textButton_26.text = '23'
            self.main_widget.ids.textButton_27.text = '24'
            self.main_widget.ids.textButton_28.text = '25'
            self.main_widget.ids.textButton_29.text = '26'
            self.main_widget.ids.textButton_30.text = '27'
            self.main_widget.ids.textButton_31.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_32.text = ''
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

            if day_finish == 29:
                self.main_widget.ids.textButton_32.text = '29'
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

            if day_finish == 30:
                self.main_widget.ids.textButton_32.text = '29'
                self.main_widget.ids.textButton_33.text = '30'
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

            if day_finish == 31:
                self.main_widget.ids.textButton_32.text = '29'
                self.main_widget.ids.textButton_33.text = '30'
                self.main_widget.ids.textButton_34.text = '31'
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

        if day_start == 4:
            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = ''
            self.main_widget.ids.textButton_3.text = ''
            self.main_widget.ids.textButton_4.text = ''
            self.main_widget.ids.textButton_5.text = '1'
            self.main_widget.ids.textButton_6.text = '2'
            self.main_widget.ids.textButton_7.text = '3'
            self.main_widget.ids.textButton_8.text = '4'
            self.main_widget.ids.textButton_9.text = '5'
            self.main_widget.ids.textButton_10.text = '6'
            self.main_widget.ids.textButton_11.text = '7'
            self.main_widget.ids.textButton_12.text = '8'
            self.main_widget.ids.textButton_13.text = '9'
            self.main_widget.ids.textButton_14.text = '10'
            self.main_widget.ids.textButton_15.text = '11'
            self.main_widget.ids.textButton_16.text = '12'
            self.main_widget.ids.textButton_17.text = '13'
            self.main_widget.ids.textButton_18.text = '14'
            self.main_widget.ids.textButton_19.text = '15'
            self.main_widget.ids.textButton_20.text = '16'
            self.main_widget.ids.textButton_21.text = '17'
            self.main_widget.ids.textButton_22.text = '18'
            self.main_widget.ids.textButton_23.text = '19'
            self.main_widget.ids.textButton_24.text = '20'
            self.main_widget.ids.textButton_25.text = '21'
            self.main_widget.ids.textButton_26.text = '22'
            self.main_widget.ids.textButton_27.text = '23'
            self.main_widget.ids.textButton_28.text = '24'
            self.main_widget.ids.textButton_29.text = '25'
            self.main_widget.ids.textButton_30.text = '26'
            self.main_widget.ids.textButton_31.text = '27'
            self.main_widget.ids.textButton_32.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_33.text = ''
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 29:
                self.main_widget.ids.textButton_33.text = '29'
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 30:
                self.main_widget.ids.textButton_33.text = '29'
                self.main_widget.ids.textButton_34.text = '30'
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 31:
                self.main_widget.ids.textButton_33.text = '29'
                self.main_widget.ids.textButton_34.text = '30'
                self.main_widget.ids.textButton_35.text = '31'
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''

        if day_start == 5:
            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = ''
            self.main_widget.ids.textButton_3.text = ''
            self.main_widget.ids.textButton_4.text = ''
            self.main_widget.ids.textButton_5.text = ''
            self.main_widget.ids.textButton_6.text = '1'
            self.main_widget.ids.textButton_7.text = '2'
            self.main_widget.ids.textButton_8.text = '3'
            self.main_widget.ids.textButton_9.text = '4'
            self.main_widget.ids.textButton_10.text = '5'
            self.main_widget.ids.textButton_11.text = '6'
            self.main_widget.ids.textButton_12.text = '7'
            self.main_widget.ids.textButton_13.text = '8'
            self.main_widget.ids.textButton_14.text = '9'
            self.main_widget.ids.textButton_15.text = '10'
            self.main_widget.ids.textButton_16.text = '11'
            self.main_widget.ids.textButton_17.text = '12'
            self.main_widget.ids.textButton_18.text = '13'
            self.main_widget.ids.textButton_19.text = '14'
            self.main_widget.ids.textButton_20.text = '15'
            self.main_widget.ids.textButton_21.text = '16'
            self.main_widget.ids.textButton_22.text = '17'
            self.main_widget.ids.textButton_23.text = '18'
            self.main_widget.ids.textButton_24.text = '19'
            self.main_widget.ids.textButton_25.text = '20'
            self.main_widget.ids.textButton_26.text = '21'
            self.main_widget.ids.textButton_27.text = '22'
            self.main_widget.ids.textButton_28.text = '23'
            self.main_widget.ids.textButton_29.text = '24'
            self.main_widget.ids.textButton_30.text = '25'
            self.main_widget.ids.textButton_31.text = '26'
            self.main_widget.ids.textButton_32.text = '27'
            self.main_widget.ids.textButton_33.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_34.text = ''
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 29:
                self.main_widget.ids.textButton_34.text = '29'
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 30:
                self.main_widget.ids.textButton_34.text = '29'
                self.main_widget.ids.textButton_35.text = '30'
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 31:
                self.main_widget.ids.textButton_34.text = '29'
                self.main_widget.ids.textButton_35.text = '30'
                self.main_widget.ids.textButton_36.text = '31'
                self.main_widget.ids.textButton_37.text = ''

        if day_start == 6:
            self.main_widget.ids.textButton_1.text = ''
            self.main_widget.ids.textButton_2.text = ''
            self.main_widget.ids.textButton_3.text = ''
            self.main_widget.ids.textButton_4.text = ''
            self.main_widget.ids.textButton_5.text = ''
            self.main_widget.ids.textButton_6.text = ''
            self.main_widget.ids.textButton_7.text = '1'
            self.main_widget.ids.textButton_8.text = '2'
            self.main_widget.ids.textButton_9.text = '3'
            self.main_widget.ids.textButton_10.text = '4'
            self.main_widget.ids.textButton_11.text = '5'
            self.main_widget.ids.textButton_12.text = '6'
            self.main_widget.ids.textButton_13.text = '7'
            self.main_widget.ids.textButton_14.text = '8'
            self.main_widget.ids.textButton_15.text = '9'
            self.main_widget.ids.textButton_16.text = '10'
            self.main_widget.ids.textButton_17.text = '11'
            self.main_widget.ids.textButton_18.text = '12'
            self.main_widget.ids.textButton_19.text = '13'
            self.main_widget.ids.textButton_20.text = '14'
            self.main_widget.ids.textButton_21.text = '15'
            self.main_widget.ids.textButton_22.text = '16'
            self.main_widget.ids.textButton_23.text = '17'
            self.main_widget.ids.textButton_24.text = '18'
            self.main_widget.ids.textButton_25.text = '19'
            self.main_widget.ids.textButton_26.text = '20'
            self.main_widget.ids.textButton_27.text = '21'
            self.main_widget.ids.textButton_28.text = '22'
            self.main_widget.ids.textButton_29.text = '23'
            self.main_widget.ids.textButton_30.text = '24'
            self.main_widget.ids.textButton_31.text = '25'
            self.main_widget.ids.textButton_32.text = '26'
            self.main_widget.ids.textButton_33.text = '27'
            self.main_widget.ids.textButton_34.text = '28'

            if day_finish == 28:
                self.main_widget.ids.textButton_35.text = ''
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 29:
                self.main_widget.ids.textButton_35.text = '29'
                self.main_widget.ids.textButton_36.text = ''
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 30:
                self.main_widget.ids.textButton_35.text = '29'
                self.main_widget.ids.textButton_36.text = '30'
                self.main_widget.ids.textButton_37.text = ''
            if day_finish == 31:
                self.main_widget.ids.textButton_35.text = '29'
                self.main_widget.ids.textButton_36.text = '30'
                self.main_widget.ids.textButton_37.text = '31'

    def previous_month(self):

        all_months = ["Unknown",
                      "Январь",
                      "Февраль",
                      "Март",
                      "Апрель",
                      "Май",
                      "Июнь",
                      "Июль",
                      "Август",
                      "Сентябрь",
                      "Октябрь",
                      "Ноябрь",
                      "Декабрь"]

        if (all_months.index(self.name_month)) == 1:
            self.name_month = all_months[(all_months.index(self.name_month)) + 11]
            self.main_widget.ids.month_label.text = all_months[(all_months.index(self.name_month))]
            self.main_widget.ids.toolbar.title = self.show_year(2)
            self.name_month = all_months[(all_months.index(self.name_month))]
            # self.name_year = self.name_year - 1
            g = calendar.monthrange(self.name_year, all_months.index(self.name_month))
            self.number_day(g[0], g[1])
        else:
            self.main_widget.ids.month_label.text = all_months[(all_months.index(self.name_month)) - 1]
            # self.main_widget.ids.month_label_1.text = all_months[(all_months.index(self.name_month)) - 1]
            self.name_month = all_months[(all_months.index(self.name_month)) - 1]
            g = calendar.monthrange(self.name_year, all_months.index(self.name_month))
            self.number_day(g[0], g[1])

    def number_month(self,month):
        all_months = ["Unknown",
                      "Январь",
                      "Февраль",
                      "Март",
                      "Апрель",
                      "Май",
                      "Июнь",
                      "Июль",
                      "Август",
                      "Сентябрь",
                      "Октябрь",
                      "Ноябрь",
                      "Декабрь"]
        self.num_month = all_months.index(month)

    def next_month(self):
        all_months = ["Unknown",
                      "Январь",
                      "Февраль",
                      "Март",
                      "Апрель",
                      "Май",
                      "Июнь",
                      "Июль",
                      "Август",
                      "Сентябрь",
                      "Октябрь",
                      "Ноябрь",
                      "Декабрь"]

        if ((all_months.index(self.name_month))) == 12:
            self.name_month = all_months[(all_months.index(self.name_month)) - 11]
            self.main_widget.ids.month_label.text = all_months[(all_months.index(self.name_month))]
            self.main_widget.ids.toolbar.title = self.show_year(1)
            self.name_month = all_months[(all_months.index(self.name_month))]
            g = calendar.monthrange(self.name_year, all_months.index(self.name_month))
            self.number_day(g[0], g[1])
        else:
            self.main_widget.ids.month_label.text = all_months[(all_months.index(self.name_month)) + 1]
            self.name_month = all_months[(all_months.index(self.name_month)) + 1]
            g = calendar.monthrange(self.name_year, all_months.index(self.name_month))
            self.number_day(g[0], g[1])

    def change_title(self, day, mounth):
        print(day,mounth,self.name_year)
        f = str(day) +' '+ str(mounth)+ ' ' + ' ' + str(self.name_year)
        self.main_widget.ids.toolbar.title = str(f)
        self.number_month(mounth)
        self.datetim = str(day) + '.' + str(self.num_month) + '.' + str(self.name_year)
        print(self.datetim)

    def theme_picker_open(self):
        if not self.md_theme_picker:
            self.md_theme_picker = MDThemePicker()
        self.md_theme_picker.open()

    def nnn(self, m, month):
        task = []
        description = []
        date = []
        self.mycursor.execute("SELECT name FROM new_schema.new_table where name_month = %s;", (month,))
        for x in self.mycursor:
            task.append(x)
        self.mycursor.execute("SELECT description FROM new_schema.new_table where name_month = %s;", (month,))
        for x in self.mycursor:
            description.append(x)
        self.mycursor.execute( "SELECT date_time FROM new_schema.new_table where name_month = %s;", (month,))
        for x in self.mycursor:
            date.append(x)

        self.lenwidget = len(task)
        i = 0
        while i < len(task):
            #m.add_widget(Factory.List_Task)
            m.add_widget(ThreeLineAvatarIconListItem(
            #    id = 'task' + str(i),

                text=str(",".join(date[i])),
                secondary_text= str(",".join(task[i])) + ' ' + \
                    str(",".join(description[i]))))
            #print(self.main_widget.ids.id_1[i].text)
            #print(id_1[i])
            #print('task' + str(i))
            #print(self.main_widget.ids.task1.text)
            i = i + 1

        del task[:]
        task[:] = []
        del description[:]
        description[:] = []
        del date[:]
        date[:] = []

    def pusto(self,m):
        m.clear_widgets()

    def example_add_stack_floating_buttons(self):
        def set_my_language(instance_button):
            toast(instance_button.icon)

        if not self.create_stack_floating_buttons:
            screen = self.main_widget.ids.scr_mngr.get_screen('main_screen')
            screen.add_widget(MDStackFloatingButtons(
                icon='android',
                floating_data={
                    'Python': 'language-python',
                    'Php': 'language-php',
                    'C++': 'language-cpp'},
                callback=set_my_language))
            self.create_stack_floating_buttons = True

    def set_chevron_back_screen(self):
        '''Sets the return chevron to the previous screen in ToolBar.'''

        self.main_widget.ids.toolbar.right_action_items = [
            ['dots-vertical', lambda x: self.root.toggle_nav_drawer()]]

    def download_progress_hide(self, instance_progress, value):
        '''Hides progress progress.'''

        self.main_widget.ids.toolbar.right_action_items = \
            [['download',
              lambda x: self.download_progress_show(instance_progress)]]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port))
                return True
            except Exception:
                return False

        if get_connect():
            link = 'https://www.python.org/ftp/python/3.5.1/' \
                   'python-3.5.1-embed-win32.zip'
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(self.directory, 'python-3.5.1.zip'),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide
            )
            progress.start(self.main_widget.ids.box_flt)
        else:
            toast('Connect error!')

    def download_complete(self):
        self.set_chevron_back_screen()
        toast('Done')

    def file_manager_open(self):
        def file_manager_open(text_item):
            previous = False if text_item == 'List' else True
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                              select_path=self.select_path,
                                              previous=previous)
            self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
            self.manager_open = True
            self.manager.open()

        MDDialog(
            title='Title', size_hint=(.8, .4), text_button_ok='List',
            text="Open manager with 'list' or 'previous' mode?",
            text_button_cancel='Previous',
            events_callback=file_manager_open).open()

    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;

        """

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False
        self.set_chevron_menu()

    def set_chevron_menu(self):
        self.main_widget.ids.toolbar.left_action_items = [
            ['menu', lambda x: self.root.toggle_nav_drawer()]]

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def callback_for_menu_items(self, text_item):
        toast(text_item)

    def add_cards(self, instance_grid_card_1):
        def callback(instance, value):
            if value and isinstance(value, int):
                toast('Set like in %d stars' % value)
            elif value and isinstance(value, str):
                toast('Repost with %s ' % value)
            elif value and isinstance(value, list):
                toast(value[1])
            else:
                toast('Delete post %s' % str(instance))

        if not self.cards_created:
            self.cards_created = True
            menu_items = [
                {'viewclass': 'MDMenuItem',
                 'text': 'Example item %d' % i,
                 'callback': self.callback_for_menu_items}
                for i in range(2)
            ]
            buttons = ['facebook', 'vk', 'twitter']

            instance_grid_card_1.add_widget(
                MDCardPost(text_post='Card with text',
                           swipe=True, callback=callback))
            instance_grid_card_1.add_widget(
                MDCardPost(
                    right_menu=menu_items, swipe=True,
                    text_post='Card with a button to open the menu MDDropDown',
                    callback=callback))
            instance_grid_card_1.add_widget(
                MDCardPost(
                    likes_stars=True, callback=callback, swipe=True,
                    text_post='Card with asterisks for voting.'))

            instance_grid_card_1.add_widget(
                MDCardPost(
                    source="./assets/kitten-1049129_1280.jpg",
                    tile_text="Little Baby",
                    tile_font_style="Headline",
                    text_post="This is my favorite cat. He's only six months "
                              "old. He loves milk and steals sausages :) "
                              "And he likes to play in the garden.",
                    with_image=True, swipe=True, callback=callback,
                    buttons=buttons))

    def update_screen(self, instance):
        def update_screen(interval):
            self.tick += 1
            if self.tick > 2:
                instance.update = True
                self.tick = 0
                self.main_widget.ids.upd_lbl.text = "New string"
                Clock.unschedule(update_screen)

        Clock.schedule_interval(update_screen, 1)

    def build(self):
        self.main_widget = Builder.load_string(main_widget_kv)
        # self.theme_cls.theme_style = 'Dark'

        self.main_widget.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)
        self.bottom_navigation_remove_mobile(self.main_widget)
        return self.main_widget

    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(
                widget.ids.bottom_navigation_desktop_1)

    def show_user_example_animation_card(self):
        def main_back_callback():
            toast('Close card')

        if not self.user_animation_card:
            self.user_animation_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar="./assets/guitar-1139397_1280.jpg",
                callback=main_back_callback)
            self.user_animation_card.box_content.add_widget(
                Factory.ContentForAnimCard())
        self.user_animation_card.open()

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar(text="This is a snackbar!").show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!",
                     button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very "
                          "long snackbar!").show()

    def show_example_input_dialog(self):
        if not self.input_dialog:
            self.input_dialog = MDInputDialog(
                title='Title', hint_text='Hint text', size_hint=(.8, .4),
                text_button_ok='Ok', events_callback=lambda x: None)
        self.input_dialog.open()

    def dialog_windofs(self):
        if not self.alert_dialog1:
            self.alert_dialog1 = MDDialog(
                title = 'Готово', size_hint=(.8, .4), text_button_ok='Ok',
                text="Задание создано успешно!", events_callback=lambda x: None
            )
        self.alert_dialog1.open()

    def dialog_exeption(self):
        if not self.alert_dialog2:
            self.alert_dialog2 = MDDialog(
                title = 'Ошибка', size_hint=(.8, .4), text_button_ok='Ok',
                text="Проверьте заполнение всех полей", events_callback=lambda x: None
            )
        self.alert_dialog2.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                title='Приветствую', size_hint=(.8, .4), text_button_ok='Ok',
                text="Это приложение создано для курсовой работы Ершовой Анны. Если вы заметили какие либо ошибки или у вас есть предложения по теме, пишите на этот адресс [b][color={COLOR}]annershova.a@gmail.com " \
                     "[/b]".format(COLOR=get_hex_from_color(
                    self.theme_cls.primary_color)), events_callback=lambda x: None)
        self.alert_dialog.open()

    def show_example_ok_cancel_dialog(self):
        if not self.ok_cancel_dialog:
            self.ok_cancel_dialog = MDDialog(
                title='Title', size_hint=(.8, .4), text_button_ok='Ok',
                text="This is Ok Cancel dialog", text_button_cancel='Cancel',
                events_callback=self.callback_for_menu_items)
        self.ok_cancel_dialog.open()

    def show_example_long_dialog(self):
        if not self.long_dialog:
            self.long_dialog = MDDialog(
                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                     "sed do eiusmod tempor incididunt ut labore et dolore "
                     "magna aliqua. Ut enim ad minim veniam, quis nostrud "
                     "exercitation ullamco laboris nisi ut aliquip ex ea "
                     "commodo consequat. Duis aute irure dolor in "
                     "reprehenderit in voluptate velit esse cillum dolore eu "
                     "fugiat nulla pariatur. Excepteur sint occaecat "
                     "cupidatat non proident, sunt in culpa qui officia "
                     "deserunt mollit anim id est laborum.",
                title='Title', size_hint=(.8, .4), text_button_ok='Yes',
                events_callback=self.callback_for_menu_items)
        self.long_dialog.open()

    def get_time_picker_data(self, instance, time):
        self.root.ids.time_label.text = str(time)
        self.previous_time = time

    def show_example_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_picker_data)

        if self.root.ids.time_picker_use_previous_time.active:
            try:
                time_dialog.set_time(self.previous_time)
            except AttributeError:
                pass
        time_dialog.open()

    def set_previous_date(self, date_obj):
        self.previous_date = date_obj
        self.root.ids.date_picker_label.text = str(date_obj)

    def show_example_date_picker(self):
        if self.root.ids.date_picker_use_previous_date.active:
            pd = self.previous_date
            try:
                MDDatePicker(self.set_previous_date,
                             pd.year, pd.month, pd.day).open()
            except AttributeError:
                MDDatePicker(self.set_previous_date).open()
        else:
            MDDatePicker(self.set_previous_date).open()

    def show_example_bottom_sheet(self):
        if not self.bs_menu_1:
            self.bs_menu_1 = MDListBottomSheet()
            self.bs_menu_1.add_item(
                "Here's an item with text only",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with text only"))
            self.bs_menu_1.add_item(
                "Here's an item with an icon",
                lambda x: self.callback_for_menu_items(
                    "Here's an item with an icon"),
                icon='clipboard-account')
            self.bs_menu_1.add_item(
                "Here's another!",
                lambda x: self.callback_for_menu_items(
                    "Here's another!"),
                icon='nfc')
        self.bs_menu_1.open()

    def show_example_grid_bottom_sheet(self):
        if not self.bs_menu_2:
            self.bs_menu_2 = MDGridBottomSheet()
            self.bs_menu_2.add_item(
                "Facebook",
                lambda x: self.callback_for_menu_items("Facebook"),
                icon_src='./assets/facebook-box.png')
            self.bs_menu_2.add_item(
                "YouTube",
                lambda x: self.callback_for_menu_items("YouTube"),
                icon_src='./assets/youtube-play.png')
            self.bs_menu_2.add_item(
                "Twitter",
                lambda x: self.callback_for_menu_items("Twitter"),
                icon_src='./assets/twitter.png')
            self.bs_menu_2.add_item(
                "Da Cloud",
                lambda x: self.callback_for_menu_items("Da Cloud"),
                icon_src='./assets/cloud-upload.png')
            self.bs_menu_2.add_item(
                "Camera",
                lambda x: self.callback_for_menu_items("Camera"),
                icon_src='./assets/camera.png')
        self.bs_menu_2.open()

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def open_settings(self, *args):
        return False


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


if __name__ == '__main__':
    KitchenSink().run()


