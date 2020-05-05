#include "lists.h"
#include <stdbool.h>
#include <stdlib.h>
/**
 *is_palindrome - Check if a linked list is palindrome
 *@head: The head of the linked list
 *Return: 1 if is palindrome or 0 is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *skp1, *skp2, *prev1, *firstHalf, *secondHalf, *middle;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	firstHalf = skp1 = skp2 = prev1 = *head;
	secondHalf = middle = NULL;

	while (skp1 && skp2 && skp2->next)
	{
		prev1 = skp1;
		skp1 = skp1->next;
		skp2 = skp2->next->next;
	}
	if (skp2 == NULL)
		secondHalf = skp1;
	else
	{
		middle = skp1;
		secondHalf = skp1->next;
	}
	prev1->next = NULL;
	reverse(&secondHalf);

	if (checkPalindrome(firstHalf, secondHalf))
		return (1);
	else
		return (0);
}
/**
 * checkPalindrome - Check if the data in the first half is equal to the
 * data in the second half
 *@half1: First half
 *@half2: Second half
 *Return: 1 if is palindrome or 0 if isn't
 */
int checkPalindrome(listint_t *half1, listint_t *half2)
{
	while (half1 || half2)
	{
		if (half1->n != half2->n || !half1 || !half2)
			return (0);
		if (half1)
			half1 = half1->next;
		if (half2)
			half2 = half2->next;
	}
	return (1);
}
/**
 *reverse - Reverse a linked list
 *@head: The head of the linked list
 */
void reverse(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *current;

	current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
