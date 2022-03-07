#include "GPIO_Config.h"

/* Generate Code */
/*
 * @func	LED_Init
 */
void LED_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;

	/* Enable GPIOA Clock */
	RCC_AHB1PeriphClockCmd(LEDControl_SetClock, ENABLE);

	/* Select GPIO Push-Pull Output Mode */
	GPIO_InitStructure.GPIO_Pin = LED_PIN;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_25MHz;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;

	GPIO_Init(LED_PORT, &GPIO_InitStructure);
}


/*
 * @func	BUTTON_Init
 */
void BUTTON_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;

	/* Enable GPIOA Clock */
	RCC_AHB1PeriphClockCmd(BUTTONControl_SetClock, ENABLE);

	/* Select GPIO Push-Pull Output Mode */
	GPIO_InitStructure.GPIO_Pin = BUTTON_PIN;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_25MHz;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;

	GPIO_Init(BUTTON_PORT, &GPIO_InitStructure);
}

/* !Generate Code */
 
/*
 * @func	LEDControl_SetStatus
 * @brief	Set Status for LED
 * @param	pGPIOx - GPIO Port number
 * 			GPIO_Pin - GPIO Pin number
 * 			status - status to write
 * @reval	none
 */
void LEDControl_SetStatus(GPIO_TypeDef* pGPIOx, uint8_t GPIO_Pin, uint8_t status)
{
	if (status == GPIO_PIN_SET)
	{
		pGPIOx->BSRRL |= (1 << GPIO_Pin);
	}
	else /*< (status == GPIO_PIN_RESET) >*/
	{
		pGPIOx->BSRRH |= (1 << GPIO_Pin);
	}
}

/*
 * @func	ButtonRead_Status
 * @brief	Read Status from Button Pin
 * @param	pGPIOx - GPIO Port number
 * 			GPIO_Pin - GPIO Pin number
 * @reval	Pin Status
 */
uint8_t ButtonRead_Status(GPIO_TypeDef* pGPIOx, uint32_t GPIO_Pin)
{
	uint8_t value;

	value = (uint8_t)(((pGPIOx->IDR) >> GPIO_Pin) & 0x00000001);

	return value;
}
