/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// JumioKycIdentityVerificationRequestModel
    /// </summary>
    [DataContract]
        public partial class JumioKycIdentityVerificationRequestModel :  IEquatable<JumioKycIdentityVerificationRequestModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="JumioKycIdentityVerificationRequestModel" /> class.
        /// </summary>
        /// <param name="errorUrl">errorUrl.</param>
        /// <param name="successUrl">successUrl.</param>
        /// <param name="sProviderFlowDrivenByClient">sProviderFlowDrivenByClient.</param>
        public JumioKycIdentityVerificationRequestModel(string errorUrl = default(string), string successUrl = default(string), bool? sProviderFlowDrivenByClient = default(bool?))
        {
            this.ErrorUrl = errorUrl;
            this.SuccessUrl = successUrl;
            this.IsProviderFlowDrivenByClient = sProviderFlowDrivenByClient;
        }
        
        /// <summary>
        /// Gets or Sets ErrorUrl
        /// </summary>
        [DataMember(Name="errorUrl", EmitDefaultValue=false)]
        public string ErrorUrl { get; set; }

        /// <summary>
        /// Gets or Sets SuccessUrl
        /// </summary>
        [DataMember(Name="successUrl", EmitDefaultValue=false)]
        public string SuccessUrl { get; set; }

        /// <summary>
        /// Gets or Sets IsProviderFlowDrivenByClient
        /// </summary>
        [DataMember(Name="isProviderFlowDrivenByClient", EmitDefaultValue=false)]
        public bool? IsProviderFlowDrivenByClient { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class JumioKycIdentityVerificationRequestModel {\n");
            sb.Append("  ErrorUrl: ").Append(ErrorUrl).Append("\n");
            sb.Append("  SuccessUrl: ").Append(SuccessUrl).Append("\n");
            sb.Append("  IsProviderFlowDrivenByClient: ").Append(IsProviderFlowDrivenByClient).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as JumioKycIdentityVerificationRequestModel);
        }

        /// <summary>
        /// Returns true if JumioKycIdentityVerificationRequestModel instances are equal
        /// </summary>
        /// <param name="input">Instance of JumioKycIdentityVerificationRequestModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(JumioKycIdentityVerificationRequestModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ErrorUrl == input.ErrorUrl ||
                    (this.ErrorUrl != null &&
                    this.ErrorUrl.Equals(input.ErrorUrl))
                ) && 
                (
                    this.SuccessUrl == input.SuccessUrl ||
                    (this.SuccessUrl != null &&
                    this.SuccessUrl.Equals(input.SuccessUrl))
                ) && 
                (
                    this.IsProviderFlowDrivenByClient == input.IsProviderFlowDrivenByClient ||
                    (this.IsProviderFlowDrivenByClient != null &&
                    this.IsProviderFlowDrivenByClient.Equals(input.IsProviderFlowDrivenByClient))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ErrorUrl != null)
                    hashCode = hashCode * 59 + this.ErrorUrl.GetHashCode();
                if (this.SuccessUrl != null)
                    hashCode = hashCode * 59 + this.SuccessUrl.GetHashCode();
                if (this.IsProviderFlowDrivenByClient != null)
                    hashCode = hashCode * 59 + this.IsProviderFlowDrivenByClient.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
