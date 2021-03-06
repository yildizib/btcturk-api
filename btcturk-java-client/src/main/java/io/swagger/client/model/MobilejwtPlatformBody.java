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
 * MobilejwtPlatformBody
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2022-06-22T13:33:34.912136+03:00[Europe/Istanbul]")
public class MobilejwtPlatformBody {
  @SerializedName("user_token")
  private String userToken = null;

  public MobilejwtPlatformBody userToken(String userToken) {
    this.userToken = userToken;
    return this;
  }

   /**
   * Get userToken
   * @return userToken
  **/
  @Schema(description = "")
  public String getUserToken() {
    return userToken;
  }

  public void setUserToken(String userToken) {
    this.userToken = userToken;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MobilejwtPlatformBody mobilejwtPlatformBody = (MobilejwtPlatformBody) o;
    return Objects.equals(this.userToken, mobilejwtPlatformBody.userToken);
  }

  @Override
  public int hashCode() {
    return Objects.hash(userToken);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MobilejwtPlatformBody {\n");
    
    sb.append("    userToken: ").append(toIndentedString(userToken)).append("\n");
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
