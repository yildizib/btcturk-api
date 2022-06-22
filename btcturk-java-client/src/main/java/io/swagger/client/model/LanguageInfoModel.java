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
 * LanguageInfoModel
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class LanguageInfoModel {
  @SerializedName("languageCulture")
  private String languageCulture = null;

  @SerializedName("version")
  private String version = null;

  public LanguageInfoModel languageCulture(String languageCulture) {
    this.languageCulture = languageCulture;
    return this;
  }

   /**
   * Get languageCulture
   * @return languageCulture
  **/
  @Schema(description = "")
  public String getLanguageCulture() {
    return languageCulture;
  }

  public void setLanguageCulture(String languageCulture) {
    this.languageCulture = languageCulture;
  }

  public LanguageInfoModel version(String version) {
    this.version = version;
    return this;
  }

   /**
   * Get version
   * @return version
  **/
  @Schema(description = "")
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LanguageInfoModel languageInfoModel = (LanguageInfoModel) o;
    return Objects.equals(this.languageCulture, languageInfoModel.languageCulture) &&
        Objects.equals(this.version, languageInfoModel.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(languageCulture, version);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LanguageInfoModel {\n");
    
    sb.append("    languageCulture: ").append(toIndentedString(languageCulture)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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