import arcade

# open the window. set the window title and dimensions (width and height)
arcade.open_window(1000,1000,"Map of Fault Blocks")

arcade.set_background_color(arcade.color.DAVY_GREY)


# start the render process
def render_fault_block(pointList):
    arcade.start_render()
    arcade.draw_polygon_filled(pointList, arcade.color.ASH_GREY)
    arcade.finish_render()


#arcade.run()