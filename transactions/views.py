from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, TransactionForm
from .models import Transaction

from django.conf import settings

User = settings.AUTH_USER_MODEL

@login_required
def home(request):
    """
       View function to display the user's home page with their transactions.
Retrieves the authenticated user's transactions and renders the home page template.
Parameters:request (HttpRequest): The HTTP request object. Returns:
HttpResponse: The HTTP response rendered from the template.
       """
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    return render(request, 'home.html', {'transactions': transactions})


@login_required
def add_transaction(request):
    """
        View function to add a new transaction for the authenticated user.
If the request method is POST, attempts to save the new transaction.
If the form is valid, assigns the current user to the transaction and saves it.
Otherwise, renders the form to add a new transaction.
Parameters: request (HttpRequest): The HTTP request object.
Returns: HttpResponse: The HTTP response rendered from the template.
"""
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

@login_required
def edit_transaction(request, pk):
    """
        View function to edit an existing transaction for the authenticated user.
Retrieves the transaction with the given primary key and user.
If the request method is POST, attempts to save the edited transaction.
If the form is valid, updates the transaction and redirects to the home page.
Otherwise, renders the form to edit the transaction.
Parameters: request (HttpRequest): The HTTP request object.
pk (int): The primary key of the transaction to be edited.
Returns: HttpResponse: The HTTP response rendered from the template.
    """
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'edit_transaction.html', {'form': form})

@login_required
def delete_transaction(request, pk):
    """
        View function to delete an existing transaction for the authenticated user.
Retrieves the transaction with the given primary key and user.
If the request method is POST, deletes the transaction and redirects to the home page.
Otherwise, renders the confirmation page for deleting the transaction.
Parameters: request (HttpRequest): The HTTP request object.
pk (int): The primary key of the transaction to be deleted.
Returns: HttpResponse: The HTTP response rendered from the template.
    """
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('home')
    return render(request, 'delete_transaction.html', {'transaction': transaction})