#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the head of the reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;

	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: is the head node of the linked list
 * Return: 1 if palindrome and 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	int res = 1;

	if (!head || !(*head) || !(*head)->next)
		return (1);

	/*getting the last and the middle node to reverse*/
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/*In case of odd number of nodes, the fast ptr will not be NuLL*/
	if (fast)
		slow = slow->next;

	slow = reverse_list(slow);
	fast = *head;

	while (slow)
	{
		if (fast->n != slow->n)
		{
			res = 0;
			break;
		}
		fast = fast->next;
		slow = slow->next;
	}

	return (res);
}
