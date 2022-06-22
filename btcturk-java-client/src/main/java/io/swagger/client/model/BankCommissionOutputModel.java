/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * BankCommissionOutputModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class BankCommissionOutputModel {
  @SerializedName("depositFee")
  private Double depositFee = null;

  @SerializedName("withdrawalFee")
  private Double withdrawalFee = null;

  @SerializedName("depositTax")
  private Double depositTax = null;

  @SerializedName("withdrawalTax")
  private Double withdrawalTax = null;

  @SerializedName("currency")
  private String currency = null;

  public BankCommissionOutputModel depositFee(Double depositFee) {
    this.depositFee = depositFee;
    return this;
  }

   /**
   * Get depositFee
   * @return depositFee
  **/
  @Schema(description = "")
  public Double getDepositFee() {
    return depositFee;
  }

  public void setDepositFee(Double depositFee) {
    this.depositFee = depositFee;
  }

  public BankCommissionOutputModel withdrawalFee(Double withdrawalFee) {
    this.withdrawalFee = withdrawalFee;
    return this;
  }

   /**
   * Get withdrawalFee
   * @return withdrawalFee
  **/
  @Schema(description = "")
  public Double getWithdrawalFee() {
    return withdrawalFee;
  }

  public void setWithdrawalFee(Double withdrawalFee) {
    this.withdrawalFee = withdrawalFee;
  }

  public BankCommissionOutputModel depositTax(Double depositTax) {
    this.depositTax = depositTax;
    return this;
  }

   /**
   * Get depositTax
   * @return depositTax
  **/
  @Schema(description = "")
  public Double getDepositTax() {
    return depositTax;
  }

  public void setDepositTax(Double depositTax) {
    this.depositTax = depositTax;
  }

  public BankCommissionOutputModel withdrawalTax(Double withdrawalTax) {
    this.withdrawalTax = withdrawalTax;
    return this;
  }

   /**
   * Get withdrawalTax
   * @return withdrawalTax
  **/
  @Schema(description = "")
  public Double getWithdrawalTax() {
    return withdrawalTax;
  }

  public void setWithdrawalTax(Double withdrawalTax) {
    this.withdrawalTax = withdrawalTax;
  }

  public BankCommissionOutputModel currency(String currency) {
    this.currency = currency;
    return this;
  }

   /**
   * Get currency
   * @return currency
  **/
  @Schema(description = "")
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BankCommissionOutputModel bankCommissionOutputModel = (BankCommissionOutputModel) o;
    return Objects.equals(this.depositFee, bankCommissionOutputModel.depositFee) &&
        Objects.equals(this.withdrawalFee, bankCommissionOutputModel.withdrawalFee) &&
        Objects.equals(this.depositTax, bankCommissionOutputModel.depositTax) &&
        Objects.equals(this.withdrawalTax, bankCommissionOutputModel.withdrawalTax) &&
        Objects.equals(this.currency, bankCommissionOutputModel.currency);
  }

  @Override
  public int hashCode() {
    return Objects.hash(depositFee, withdrawalFee, depositTax, withdrawalTax, currency);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BankCommissionOutputModel {\n");
    
    sb.append("    depositFee: ").append(toIndentedString(depositFee)).append("\n");
    sb.append("    withdrawalFee: ").append(toIndentedString(withdrawalFee)).append("\n");
    sb.append("    depositTax: ").append(toIndentedString(depositTax)).append("\n");
    sb.append("    withdrawalTax: ").append(toIndentedString(withdrawalTax)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
