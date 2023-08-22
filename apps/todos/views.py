from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Todo
import http
from .forms import TodoForm, TodoCompleteForm
from turbo_response import TurboStreamResponse, TurboStream


# Create your views here.
class IndexView(TemplateView):
    template_name = 'todos/index.html'
    todos = None

    def dispatch(self, request, *args, **kwargs):
        self.todos = Todo.objects.all()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        status = http.HTTPStatus.OK
        form = TodoForm()

        return self.render_to_response({
            'todos': self.todos,
            'form': form
        }, status=status)

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save()
            status = http.HTTPStatus.CREATED
            return TurboStreamResponse([
                TurboStream("todos").prepend.template("components/_todo_item.html", {
                    'todo': todo
                }).response(request).rendered_content
            ], status=status)

        status = http.HTTPStatus.UNPROCESSABLE_ENTITY

        return self.render_to_response({
            'form': form,
            'todos': self.todos
        }, status=status)


class DeleteTodo(TemplateView):
    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, id=kwargs['id'])
        todo.delete()
        return TurboStreamResponse([
            TurboStream(f"todo-{kwargs['id']}-item").remove.render()
        ])


class UpdateTodo(TemplateView):
    template_name = 'components/_todo_form.html'
    def dispatch(self, request, *args, **kwargs):
        self.todo = get_object_or_404(Todo, id=kwargs['id'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TodoForm(instance=self.todo)
        print(request.turbo.frame)
        return self.render_to_response({
            'form': form,
            'todo': self.todo
        })

    def post(self, request, *args, **kwargs):
        form = TodoForm(data=request.POST, instance=self.todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')

        return self.render_to_response({
            'form': form,
            'todo': self.todo
        })


class CompleteTodo(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.todo = get_object_or_404(Todo, id=kwargs['id'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TodoCompleteForm(instance=self.todo)
        return self.render_to_response({
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TodoCompleteForm(data=request.POST, instance=self.todo)

        if form.is_valid():
            form.save()
            return redirect('todos:index')
        return self.render_to_response({
            'form': form,
            'todo': self.todo
        })