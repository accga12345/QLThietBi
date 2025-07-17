from controller.deviceController import DeviceController
from view.view import DeviceView

def main():
    controller = DeviceController()
    view = DeviceView(controller)
    controller.set_view(view)
    view.root.mainloop()

if __name__ == "__main__":
    main()
