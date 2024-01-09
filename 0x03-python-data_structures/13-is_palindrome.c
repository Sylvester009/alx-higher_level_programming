#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_list - Reverses a singly-linked listint_t list.
* @head: A pointer to the starting head node
*
* Return: A pointer to the head
*/

listint_t *reverse_list(listint_t **head)
{
listint_t *current = *head, *next, *prev = NULL;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the list.
*
* Return: If the linked list is a palindrome - 1.
*         Else - 1.
*/

int is_palindrome(listint_t **head)
{
listint_t *tmp = *head, *per = *head, *reversed = NULL;
size_t size = 0;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (per && per->next)
{
tmp = tmp->next;
per = per->next->next;
}

listint_t *current = tmp, *next, *prev = NULL;
while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
reversed = prev;

listint_t *temp = *head;
while (reversed)
{
if (temp->n != reversed->n)
return (0);

temp = temp->next;
reversed = reversed->next;
}

return (1);
}
