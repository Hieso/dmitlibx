from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def create_vk_keyboard(options,leave):
    keyboard = VkKeyboard(one_time=True)
    for option in options:
        keyboard.add_button(option, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
    keyboard.add_button(leave, color=VkKeyboardColor.SECONDARY)
    return keyboard