#include "lists.h"
/**
* check_cycle - checking for a cycle in linked list
* @list: linked list to check
*
* Return: 1 if true and 0 if false
*/

int check_cycle(listint_t *list)
{
	listint_t *slowing = list;
	listint_t *fasting = list;

	if (!list)
		return (0);;

	while (slowing && fasting && fasting->next)
	{
		slowing = slowing->next;
		fasting = fasting->next->next;
		if (slowing == fasting)
			return (1);
	}

	return (0);
}
