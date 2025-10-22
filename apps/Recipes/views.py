from django.shortcuts import render,redirect,get_object_or_404
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
def addRecipe(request):
    if request.method=="POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return redirect('add')
    else:
        form = RecipeForm()
    s = Recipe.objects.all()
    return render(request,"Recipes/addrecipes.html",{'form':form ,'s':s})
    
def UpdateRecipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('add')  # redirect to your desired page

    return render(request, "Recipes/update.html", {'form': form})

def delete(request,id):
    r = get_object_or_404(Recipe,id=id)
    if request.method=="POST":
        r.delete()
        return redirect('add')
    return render(request,"Recipes/delete.html",{'r':r})
 