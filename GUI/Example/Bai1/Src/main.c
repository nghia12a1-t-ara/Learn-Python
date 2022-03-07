/**
  ******************************************************************************
  * @file    main.c
  * @author  Auto-generated by STM32CubeIDE
  * @version V1.0
  * @brief   Default main function.
  ******************************************************************************
*/

#include "stm32f401re.h"
#include "stm32f401re_rcc.h"
#include "stm32f401re_gpio.h"
#include "GPIO_Config.h"

void delay_ms(uint32_t);

int main(void)
{
	LED_Init();
	BUTTON_Init();
	uint8_t led_state = 0;

	while(1)
	{
		if (ButtonRead_Status(BUTTON_PORT, BUTTON_PIN13) == GPIO_PIN_LOW)
		{
			delay_ms(20);
			while (ButtonRead_Status(BUTTON_PORT, BUTTON_PIN13) == GPIO_PIN_LOW);
			if (led_state == GPIO_PIN_LOW)
			{
				led_state = GPIO_PIN_HIGH;
			}
			else /*< (led_state == GPIO_PIN_HIGH) >*/
			{
				led_state = GPIO_PIN_LOW;
			}
			LEDControl_SetStatus(LED_PORT, LED_PIN5, led_state);
		}
	}
}

void delay_ms(uint32_t time)
{
	while(time--)
	{
		for (uint32_t i = 0; i < 5000; i++);
	}
}