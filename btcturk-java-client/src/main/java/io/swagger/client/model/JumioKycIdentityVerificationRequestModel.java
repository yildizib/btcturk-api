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
 * JumioKycIdentityVerificationRequestModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class JumioKycIdentityVerificationRequestModel {
  @SerializedName("errorUrl")
  private String errorUrl = null;

  @SerializedName("successUrl")
  private String successUrl = null;

  @SerializedName("isProviderFlowDrivenByClient")
  private Boolean ısProviderFlowDrivenByClient = null;

  public JumioKycIdentityVerificationRequestModel errorUrl(String errorUrl) {
    this.errorUrl = errorUrl;
    return this;
  }

   /**
   * Get errorUrl
   * @return errorUrl
  **/
  @Schema(description = "")
  public String getErrorUrl() {
    return errorUrl;
  }

  public void setErrorUrl(String errorUrl) {
    this.errorUrl = errorUrl;
  }

  public JumioKycIdentityVerificationRequestModel successUrl(String successUrl) {
    this.successUrl = successUrl;
    return this;
  }

   /**
   * Get successUrl
   * @return successUrl
  **/
  @Schema(description = "")
  public String getSuccessUrl() {
    return successUrl;
  }

  public void setSuccessUrl(String successUrl) {
    this.successUrl = successUrl;
  }

  public JumioKycIdentityVerificationRequestModel ısProviderFlowDrivenByClient(Boolean ısProviderFlowDrivenByClient) {
    this.ısProviderFlowDrivenByClient = ısProviderFlowDrivenByClient;
    return this;
  }

   /**
   * Get ısProviderFlowDrivenByClient
   * @return ısProviderFlowDrivenByClient
  **/
  @Schema(description = "")
  public Boolean isIsProviderFlowDrivenByClient() {
    return ısProviderFlowDrivenByClient;
  }

  public void setIsProviderFlowDrivenByClient(Boolean ısProviderFlowDrivenByClient) {
    this.ısProviderFlowDrivenByClient = ısProviderFlowDrivenByClient;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    JumioKycIdentityVerificationRequestModel jumioKycIdentityVerificationRequestModel = (JumioKycIdentityVerificationRequestModel) o;
    return Objects.equals(this.errorUrl, jumioKycIdentityVerificationRequestModel.errorUrl) &&
        Objects.equals(this.successUrl, jumioKycIdentityVerificationRequestModel.successUrl) &&
        Objects.equals(this.ısProviderFlowDrivenByClient, jumioKycIdentityVerificationRequestModel.ısProviderFlowDrivenByClient);
  }

  @Override
  public int hashCode() {
    return Objects.hash(errorUrl, successUrl, ısProviderFlowDrivenByClient);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class JumioKycIdentityVerificationRequestModel {\n");
    
    sb.append("    errorUrl: ").append(toIndentedString(errorUrl)).append("\n");
    sb.append("    successUrl: ").append(toIndentedString(successUrl)).append("\n");
    sb.append("    ısProviderFlowDrivenByClient: ").append(toIndentedString(ısProviderFlowDrivenByClient)).append("\n");
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
