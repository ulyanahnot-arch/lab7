from todo_model import TaskModel
from todo_view import TaskView
from todo_controller import TaskController

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    controller.run()

if __name__ == "__main__":
    main()