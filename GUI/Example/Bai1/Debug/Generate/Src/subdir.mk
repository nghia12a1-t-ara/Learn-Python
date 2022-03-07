################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Generate/Src/GPIO_Config.c 

OBJS += \
./Generate/Src/GPIO_Config.o 

C_DEPS += \
./Generate/Src/GPIO_Config.d 


# Each subdirectory must supply rules for building sources it contributes
Generate/Src/GPIO_Config.o: ../Generate/Src/GPIO_Config.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F401RETx -DSTM32F4 -DDEBUG -c -I../Inc -I"D:/Python/Python_Repo/Learn-Python/GUI/Example/Bai1/Inc" -I"D:/Python/Python_Repo/Learn-Python/GUI/Example/Bai1/Generate/Inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/CMSIS/Include" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/STM32F401RE_StdPeriph_Driver/inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/button" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/led" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Utilities" -I"D:/Python/Python_Repo/Learn-Python/GUI/Example/Bai1/Inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Generate/Src/GPIO_Config.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

