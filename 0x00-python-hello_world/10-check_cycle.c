#include "lists.h"

/**
* check_cycle - checks if singly linked list has a cycle.
* @list: head of list
* Description - check for loops in list
* Return: 1 (no-cycle) else 0 (cycle)
*/

int check_cycle(listint_t *list)
{
	listint_t *s;
	listint_t *f;

	if (!list)
		return (0);

	s = list;
	f = list->next;
	while (f && s && f->next)
	{
		s = s->next;
		f = f->next->next;
		
		if (s == f)
		{
			return (1);
		}
	}
	return (0);
}
