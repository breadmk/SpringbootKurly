package kr.co.doogle.dto;

import java.util.Date;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class OrdersPaymentDTO {
	
	private int ono, payment;
	private String type;
	private Date writedate;

}
