/*
 * _24FC512.c
 *
 * Created: 2021-11-29 오후 12:57:07
 *  Author: Tae Min Shin
 */ 
#define F_CPU	5000000UL		// Max System Clock Frequency at 1.8V ~ 5.5V VDD

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <avr/sfr_defs.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "twi.h"
#include "D24FC512.h"

uint8_t EEPROM_ReadByte( uint16_t adr ) {
	return I2C_readAddress_Byte( D24FC512_ADDR, adr );
}

uint16_t EEPROM_ReadUint16( uint16_t adr ) {
	return I2C_readAddress_Uint16( D24FC512_ADDR, adr );
}

void EEPROM_ReadBlock( uint16_t adr, uint8_t *buffer, uint8_t len ) {
	I2C_readAddress_Block( D24FC512_ADDR, adr, buffer, len );	
}

void EEPROM_WriteByte( uint16_t adr, uint8_t dat ) {
	I2C_writeAddress_Byte( D24FC512_ADDR, adr, dat );
}

void EEPROM_WriteUint16( uint16_t adr, uint16_t dat ) {
	I2C_writeAddress_Uint16( D24FC512_ADDR, adr, dat );
}

void EEPROM_WritePage( uint16_t adr, uint8_t *buffer, uint8_t len ) {
	uint16_t	pageStart, pageEnd;
	
	pageStart = adr & 0xff80;
	pageEnd = pageStart + 128;
	if ( (adr + len) <= pageEnd ) 
		I2C_writeAddress_Block( D24FC512_ADDR, adr, buffer, len );
	else
		I2C_writeAddress_Block( D24FC512_ADDR, adr, buffer, pageEnd - adr );
}
