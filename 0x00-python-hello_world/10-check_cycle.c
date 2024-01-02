#include "lists.h"

/**
* check_cycle - checks if singly linked list has a cycle.
* @list: head of list
* Description - check for loops in list
* Return: 1 (no-cycle) else 0 (cycle)
*/

int check_cycle(listint_t *list)
{
struct listint_t *t, *j;

t = list;
j = list->next;
  
if (!list)
return (0);

while (j && t && j->next)
{
if (t == j)
{
return (1);
}
j = j->next;
t = t->next->next;
}
return (0);
}
