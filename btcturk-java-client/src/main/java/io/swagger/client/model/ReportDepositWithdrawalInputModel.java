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
import io.swagger.client.model.DocumentFileType;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;
/**
 * ReportDepositWithdrawalInputModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class ReportDepositWithdrawalInputModel {
  @SerializedName("types")
  private List<Integer> types = null;

  @SerializedName("currencies")
  private List<Integer> currencies = null;

  @SerializedName("beginDate")
  private OffsetDateTime beginDate = null;

  @SerializedName("endDate")
  private OffsetDateTime endDate = null;

  @SerializedName("documentFileType")
  private DocumentFileType documentFileType = null;

  public ReportDepositWithdrawalInputModel types(List<Integer> types) {
    this.types = types;
    return this;
  }

  public ReportDepositWithdrawalInputModel addTypesItem(Integer typesItem) {
    if (this.types == null) {
      this.types = new ArrayList<Integer>();
    }
    this.types.add(typesItem);
    return this;
  }

   /**
   * Get types
   * @return types
  **/
  @Schema(description = "")
  public List<Integer> getTypes() {
    return types;
  }

  public void setTypes(List<Integer> types) {
    this.types = types;
  }

  public ReportDepositWithdrawalInputModel currencies(List<Integer> currencies) {
    this.currencies = currencies;
    return this;
  }

  public ReportDepositWithdrawalInputModel addCurrenciesItem(Integer currenciesItem) {
    if (this.currencies == null) {
      this.currencies = new ArrayList<Integer>();
    }
    this.currencies.add(currenciesItem);
    return this;
  }

   /**
   * Get currencies
   * @return currencies
  **/
  @Schema(description = "")
  public List<Integer> getCurrencies() {
    return currencies;
  }

  public void setCurrencies(List<Integer> currencies) {
    this.currencies = currencies;
  }

  public ReportDepositWithdrawalInputModel beginDate(OffsetDateTime beginDate) {
    this.beginDate = beginDate;
    return this;
  }

   /**
   * Get beginDate
   * @return beginDate
  **/
  @Schema(description = "")
  public OffsetDateTime getBeginDate() {
    return beginDate;
  }

  public void setBeginDate(OffsetDateTime beginDate) {
    this.beginDate = beginDate;
  }

  public ReportDepositWithdrawalInputModel endDate(OffsetDateTime endDate) {
    this.endDate = endDate;
    return this;
  }

   /**
   * Get endDate
   * @return endDate
  **/
  @Schema(description = "")
  public OffsetDateTime getEndDate() {
    return endDate;
  }

  public void setEndDate(OffsetDateTime endDate) {
    this.endDate = endDate;
  }

  public ReportDepositWithdrawalInputModel documentFileType(DocumentFileType documentFileType) {
    this.documentFileType = documentFileType;
    return this;
  }

   /**
   * Get documentFileType
   * @return documentFileType
  **/
  @Schema(description = "")
  public DocumentFileType getDocumentFileType() {
    return documentFileType;
  }

  public void setDocumentFileType(DocumentFileType documentFileType) {
    this.documentFileType = documentFileType;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReportDepositWithdrawalInputModel reportDepositWithdrawalInputModel = (ReportDepositWithdrawalInputModel) o;
    return Objects.equals(this.types, reportDepositWithdrawalInputModel.types) &&
        Objects.equals(this.currencies, reportDepositWithdrawalInputModel.currencies) &&
        Objects.equals(this.beginDate, reportDepositWithdrawalInputModel.beginDate) &&
        Objects.equals(this.endDate, reportDepositWithdrawalInputModel.endDate) &&
        Objects.equals(this.documentFileType, reportDepositWithdrawalInputModel.documentFileType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(types, currencies, beginDate, endDate, documentFileType);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReportDepositWithdrawalInputModel {\n");
    
    sb.append("    types: ").append(toIndentedString(types)).append("\n");
    sb.append("    currencies: ").append(toIndentedString(currencies)).append("\n");
    sb.append("    beginDate: ").append(toIndentedString(beginDate)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    documentFileType: ").append(toIndentedString(documentFileType)).append("\n");
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
