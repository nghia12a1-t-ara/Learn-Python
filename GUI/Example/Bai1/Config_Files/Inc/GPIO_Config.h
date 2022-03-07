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
#define $(Peripheral_Name)$_PORT						$(Peripheral)$
#define $(Peripheral_Name)$_PIN						GPIO_Pin_$(Pin_Number)$
#define $(Peripheral_Name)$_PIN$(Pin_Number)$						$(Pin_Number)$
#define $(Peripheral_Name)$Control_SetClock						RCC_AHB1Periph_$(Peripheral)$
/*
 * Function Prototypes Generate
 */
void $(Peripheral_Name)$_Init(void);
/* !Generate Code */
 
/*
 * Function Prototypes
 */
void LEDControl_SetStatus(GPIO_TypeDef*, uint8_t, uint8_t);
uint8_t ButtonRead_Status(GPIO_TypeDef*, uint32_t);

#endif /* _GPIO_CONFIG_H_ */
