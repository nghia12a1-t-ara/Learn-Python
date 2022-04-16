################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Generate/Src/GPIO_Config.c 

OBJS += \
./Generate/Src/GPIO_Config.o 

C_DEPS += \
./Generate/Src/GPIO_Config.d 


# Each subdirectory must supply rules for building sources it contributes
Generate/Src/GPIO_Config.o: ../Generate/Src/GPIO_Config.c Generate/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DSTM32 -DSTM32F401RETx -DSTM32F4 -DDEBUG -c -I../Inc -I"D:/STM32/STM32_SourceCode/MPU/Learn-Python/GUI/Example/Bai1/Generate/Inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/CMSIS/Include" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Drivers/STM32F401RE_StdPeriph_Driver/inc" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/button" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Middle/led" -I"D:/IOT302_Funix/SDK_1.0.3_NUCLEO-F401RE/shared/Utilities" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Generate/Src/GPIO_Config.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

