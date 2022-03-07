#ifndef _GPIO_CONFIG_H_
#define _GPIO_CONFIG_H_

#include "stm32f401re.h"
#include "stm32f401re_rcc.h"
#include "stm32f401re_gpio.h"

/*
 * Define Logic GPIO Pin
 */
#define GPIO_PIN_SET	1
#define GPIO_PIN_RESET	0
#define GPIO_PIN_LOW	0
#define GPIO_PIN_HIGH	1

/* Generate Code */
#define LED_PORT						GPIOA
#define LED_PIN						GPIO_Pin_5
#define LED_PIN5						5
#define LEDControl_SetClock						RCC_AHB1Periph_GPIOA
/*
 * Function Prototypes Generate
 */
void LED_Init(void);


#define BUTTON_PORT						GPIOC
#define BUTTON_PIN						GPIO_Pin_13
#define BUTTON_PIN13						13
#define BUTTONControl_SetClock						RCC_AHB1Periph_GPIOC
/*
 * Function Prototypes Generate
 */
void BUTTON_Init(void);

/* !Generate Code */
 
/*
 * Function Prototypes
 */
void LEDControl_SetStatus(GPIO_TypeDef*, uint8_t, uint8_t);
uint8_t ButtonRead_Status(GPIO_TypeDef*, uint32_t);

#endif /* _GPIO_CONFIG_H_ */
