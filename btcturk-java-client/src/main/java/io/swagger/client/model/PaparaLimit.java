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
 * PaparaLimit
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class PaparaLimit {
  @SerializedName("maxDepositFeeAmount")
  private Double maxDepositFeeAmount = null;

  @SerializedName("minDepositAmount")
  private Double minDepositAmount = null;

  @SerializedName("maxDepositAmount")
  private Double maxDepositAmount = null;

  @SerializedName("minWithdrawalAmounts")
  private Double minWithdrawalAmounts = null;

  @SerializedName("maxWithdrawalFeeAmount")
  private Double maxWithdrawalFeeAmount = null;

  @SerializedName("minWithdrawalPerTransaction")
  private Double minWithdrawalPerTransaction = null;

  public PaparaLimit maxDepositFeeAmount(Double maxDepositFeeAmount) {
    this.maxDepositFeeAmount = maxDepositFeeAmount;
    return this;
  }

   /**
   * Get maxDepositFeeAmount
   * @return maxDepositFeeAmount
  **/
  @Schema(description = "")
  public Double getMaxDepositFeeAmount() {
    return maxDepositFeeAmount;
  }

  public void setMaxDepositFeeAmount(Double maxDepositFeeAmount) {
    this.maxDepositFeeAmount = maxDepositFeeAmount;
  }

  public PaparaLimit minDepositAmount(Double minDepositAmount) {
    this.minDepositAmount = minDepositAmount;
    return this;
  }

   /**
   * Get minDepositAmount
   * @return minDepositAmount
  **/
  @Schema(description = "")
  public Double getMinDepositAmount() {
    return minDepositAmount;
  }

  public void setMinDepositAmount(Double minDepositAmount) {
    this.minDepositAmount = minDepositAmount;
  }

  public PaparaLimit maxDepositAmount(Double maxDepositAmount) {
    this.maxDepositAmount = maxDepositAmount;
    return this;
  }

   /**
   * Get maxDepositAmount
   * @return maxDepositAmount
  **/
  @Schema(description = "")
  public Double getMaxDepositAmount() {
    return maxDepositAmount;
  }

  public void setMaxDepositAmount(Double maxDepositAmount) {
    this.maxDepositAmount = maxDepositAmount;
  }

  public PaparaLimit minWithdrawalAmounts(Double minWithdrawalAmounts) {
    this.minWithdrawalAmounts = minWithdrawalAmounts;
    return this;
  }

   /**
   * Get minWithdrawalAmounts
   * @return minWithdrawalAmounts
  **/
  @Schema(description = "")
  public Double getMinWithdrawalAmounts() {
    return minWithdrawalAmounts;
  }

  public void setMinWithdrawalAmounts(Double minWithdrawalAmounts) {
    this.minWithdrawalAmounts = minWithdrawalAmounts;
  }

  public PaparaLimit maxWithdrawalFeeAmount(Double maxWithdrawalFeeAmount) {
    this.maxWithdrawalFeeAmount = maxWithdrawalFeeAmount;
    return this;
  }

   /**
   * Get maxWithdrawalFeeAmount
   * @return maxWithdrawalFeeAmount
  **/
  @Schema(description = "")
  public Double getMaxWithdrawalFeeAmount() {
    return maxWithdrawalFeeAmount;
  }

  public void setMaxWithdrawalFeeAmount(Double maxWithdrawalFeeAmount) {
    this.maxWithdrawalFeeAmount = maxWithdrawalFeeAmount;
  }

  public PaparaLimit minWithdrawalPerTransaction(Double minWithdrawalPerTransaction) {
    this.minWithdrawalPerTransaction = minWithdrawalPerTransaction;
    return this;
  }

   /**
   * Get minWithdrawalPerTransaction
   * @return minWithdrawalPerTransaction
  **/
  @Schema(description = "")
  public Double getMinWithdrawalPerTransaction() {
    return minWithdrawalPerTransaction;
  }

  public void setMinWithdrawalPerTransaction(Double minWithdrawalPerTransaction) {
    this.minWithdrawalPerTransaction = minWithdrawalPerTransaction;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PaparaLimit paparaLimit = (PaparaLimit) o;
    return Objects.equals(this.maxDepositFeeAmount, paparaLimit.maxDepositFeeAmount) &&
        Objects.equals(this.minDepositAmount, paparaLimit.minDepositAmount) &&
        Objects.equals(this.maxDepositAmount, paparaLimit.maxDepositAmount) &&
        Objects.equals(this.minWithdrawalAmounts, paparaLimit.minWithdrawalAmounts) &&
        Objects.equals(this.maxWithdrawalFeeAmount, paparaLimit.maxWithdrawalFeeAmount) &&
        Objects.equals(this.minWithdrawalPerTransaction, paparaLimit.minWithdrawalPerTransaction);
  }

  @Override
  public int hashCode() {
    return Objects.hash(maxDepositFeeAmount, minDepositAmount, maxDepositAmount, minWithdrawalAmounts, maxWithdrawalFeeAmount, minWithdrawalPerTransaction);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PaparaLimit {\n");
    
    sb.append("    maxDepositFeeAmount: ").append(toIndentedString(maxDepositFeeAmount)).append("\n");
    sb.append("    minDepositAmount: ").append(toIndentedString(minDepositAmount)).append("\n");
    sb.append("    maxDepositAmount: ").append(toIndentedString(maxDepositAmount)).append("\n");
    sb.append("    minWithdrawalAmounts: ").append(toIndentedString(minWithdrawalAmounts)).append("\n");
    sb.append("    maxWithdrawalFeeAmount: ").append(toIndentedString(maxWithdrawalFeeAmount)).append("\n");
    sb.append("    minWithdrawalPerTransaction: ").append(toIndentedString(minWithdrawalPerTransaction)).append("\n");
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
