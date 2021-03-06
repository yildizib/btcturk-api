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
import io.swagger.client.model.CurrencyType;
import io.swagger.client.model.LevelLimits;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
/**
 * CurrencyLimit
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class CurrencyLimit {
  @SerializedName("symbol")
  private String symbol = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("minDeposit")
  private Double minDeposit = null;

  @SerializedName("minWithdrawal")
  private Double minWithdrawal = null;

  @SerializedName("levelLimits")
  private LevelLimits levelLimits = null;

  @SerializedName("type")
  private CurrencyType type = null;

  @SerializedName("order")
  private Integer order = null;

  public CurrencyLimit symbol(String symbol) {
    this.symbol = symbol;
    return this;
  }

   /**
   * Get symbol
   * @return symbol
  **/
  @Schema(description = "")
  public String getSymbol() {
    return symbol;
  }

  public void setSymbol(String symbol) {
    this.symbol = symbol;
  }

  public CurrencyLimit name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
   * @return name
  **/
  @Schema(description = "")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public CurrencyLimit minDeposit(Double minDeposit) {
    this.minDeposit = minDeposit;
    return this;
  }

   /**
   * Get minDeposit
   * @return minDeposit
  **/
  @Schema(description = "")
  public Double getMinDeposit() {
    return minDeposit;
  }

  public void setMinDeposit(Double minDeposit) {
    this.minDeposit = minDeposit;
  }

  public CurrencyLimit minWithdrawal(Double minWithdrawal) {
    this.minWithdrawal = minWithdrawal;
    return this;
  }

   /**
   * Get minWithdrawal
   * @return minWithdrawal
  **/
  @Schema(description = "")
  public Double getMinWithdrawal() {
    return minWithdrawal;
  }

  public void setMinWithdrawal(Double minWithdrawal) {
    this.minWithdrawal = minWithdrawal;
  }

  public CurrencyLimit levelLimits(LevelLimits levelLimits) {
    this.levelLimits = levelLimits;
    return this;
  }

   /**
   * Get levelLimits
   * @return levelLimits
  **/
  @Schema(description = "")
  public LevelLimits getLevelLimits() {
    return levelLimits;
  }

  public void setLevelLimits(LevelLimits levelLimits) {
    this.levelLimits = levelLimits;
  }

  public CurrencyLimit type(CurrencyType type) {
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @Schema(description = "")
  public CurrencyType getType() {
    return type;
  }

  public void setType(CurrencyType type) {
    this.type = type;
  }

  public CurrencyLimit order(Integer order) {
    this.order = order;
    return this;
  }

   /**
   * Get order
   * @return order
  **/
  @Schema(description = "")
  public Integer getOrder() {
    return order;
  }

  public void setOrder(Integer order) {
    this.order = order;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CurrencyLimit currencyLimit = (CurrencyLimit) o;
    return Objects.equals(this.symbol, currencyLimit.symbol) &&
        Objects.equals(this.name, currencyLimit.name) &&
        Objects.equals(this.minDeposit, currencyLimit.minDeposit) &&
        Objects.equals(this.minWithdrawal, currencyLimit.minWithdrawal) &&
        Objects.equals(this.levelLimits, currencyLimit.levelLimits) &&
        Objects.equals(this.type, currencyLimit.type) &&
        Objects.equals(this.order, currencyLimit.order);
  }

  @Override
  public int hashCode() {
    return Objects.hash(symbol, name, minDeposit, minWithdrawal, levelLimits, type, order);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CurrencyLimit {\n");
    
    sb.append("    symbol: ").append(toIndentedString(symbol)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    minDeposit: ").append(toIndentedString(minDeposit)).append("\n");
    sb.append("    minWithdrawal: ").append(toIndentedString(minWithdrawal)).append("\n");
    sb.append("    levelLimits: ").append(toIndentedString(levelLimits)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    order: ").append(toIndentedString(order)).append("\n");
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
