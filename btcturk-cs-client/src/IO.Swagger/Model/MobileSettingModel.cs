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
    /// MobileSettingModel
    /// </summary>
    [DataContract]
        public partial class MobileSettingModel :  IEquatable<MobileSettingModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MobileSettingModel" /> class.
        /// </summary>
        /// <param name="languageSettings">languageSettings.</param>
        /// <param name="rating">rating.</param>
        /// <param name="euroIsEnable">euroIsEnable.</param>
        /// <param name="countryCode">countryCode.</param>
        public MobileSettingModel(LanguageSettingModel languageSettings = default(LanguageSettingModel), bool? rating = default(bool?), bool? euroIsEnable = default(bool?), string countryCode = default(string))
        {
            this.LanguageSettings = languageSettings;
            this.Rating = rating;
            this.EuroIsEnable = euroIsEnable;
            this.CountryCode = countryCode;
        }
        
        /// <summary>
        /// Gets or Sets LanguageSettings
        /// </summary>
        [DataMember(Name="languageSettings", EmitDefaultValue=false)]
        public LanguageSettingModel LanguageSettings { get; set; }

        /// <summary>
        /// Gets or Sets Rating
        /// </summary>
        [DataMember(Name="rating", EmitDefaultValue=false)]
        public bool? Rating { get; set; }

        /// <summary>
        /// Gets or Sets EuroIsEnable
        /// </summary>
        [DataMember(Name="euroIsEnable", EmitDefaultValue=false)]
        public bool? EuroIsEnable { get; set; }

        /// <summary>
        /// Gets or Sets CountryCode
        /// </summary>
        [DataMember(Name="countryCode", EmitDefaultValue=false)]
        public string CountryCode { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MobileSettingModel {\n");
            sb.Append("  LanguageSettings: ").Append(LanguageSettings).Append("\n");
            sb.Append("  Rating: ").Append(Rating).Append("\n");
            sb.Append("  EuroIsEnable: ").Append(EuroIsEnable).Append("\n");
            sb.Append("  CountryCode: ").Append(CountryCode).Append("\n");
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
            return this.Equals(input as MobileSettingModel);
        }

        /// <summary>
        /// Returns true if MobileSettingModel instances are equal
        /// </summary>
        /// <param name="input">Instance of MobileSettingModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MobileSettingModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.LanguageSettings == input.LanguageSettings ||
                    (this.LanguageSettings != null &&
                    this.LanguageSettings.Equals(input.LanguageSettings))
                ) && 
                (
                    this.Rating == input.Rating ||
                    (this.Rating != null &&
                    this.Rating.Equals(input.Rating))
                ) && 
                (
                    this.EuroIsEnable == input.EuroIsEnable ||
                    (this.EuroIsEnable != null &&
                    this.EuroIsEnable.Equals(input.EuroIsEnable))
                ) && 
                (
                    this.CountryCode == input.CountryCode ||
                    (this.CountryCode != null &&
                    this.CountryCode.Equals(input.CountryCode))
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
                if (this.LanguageSettings != null)
                    hashCode = hashCode * 59 + this.LanguageSettings.GetHashCode();
                if (this.Rating != null)
                    hashCode = hashCode * 59 + this.Rating.GetHashCode();
                if (this.EuroIsEnable != null)
                    hashCode = hashCode * 59 + this.EuroIsEnable.GetHashCode();
                if (this.CountryCode != null)
                    hashCode = hashCode * 59 + this.CountryCode.GetHashCode();
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